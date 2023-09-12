from typing import Any
import abc

import openai
from azure.search.documents import SearchClient
from azure.search.documents.models import QueryType

from .core.messagebuilder import MessageBuilder
from .core.modelhelper import get_token_limit

def nonewlines(s: str) -> str:
    return s.replace('\n', ' ').replace('\r', ' ')

class ChatApproach(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def run(self, history: list[dict], overrides: dict[str, Any]) -> Any:
        ...

class ChatReadRetrieveReadApproach(ChatApproach):
    # Chat roles
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

    # Simple retrieve-then-read implementation, using the Cognitive Search and OpenAI APIs directly. It first retrieves
    # top documents from search, then constructs a prompt with them, and then uses OpenAI to generate an completion
    # (answer) with that prompt.

    system_message_chat_conversation = """You are an intelligent assistant helping Unilever employees in the Competitor Intelligence group with their questions about the annual reports of Unilever and its competitors (for example: P&G, Colgate, etc.). Be brief in your answers.
Answer ONLY with the facts listed in the list of sources below. If there isn't enough information below, say you don't know. Do not generate answers that don't use the sources below. If asking a clarifying question to the user would help, ask the question.
When information can be tabulated, return it as an html table. Do not return markdown format. If the question is not in English, answer in the language used in the question.
For ordered data, return it as a numbered list. For non-ordered data or summaries, use bullet points.
Each source has a name followed by colon and the actual information, always include the source name for each fact you use in the response. Use square brackets to reference the source, e.g. [info1.txt]. Don't combine sources, list each source separately, e.g. [info1.txt][info2.pdf].
Provide actionable insights and recommendations for the user. If a persona isn't specified, answer the question as if you were a data analyst for the competitor intelligence group at Unilever.
When making recommendations and inferences explain your thought process step by step.
    
{follow_up_questions_prompt}
{injected_prompt}
"""
    follow_up_questions_prompt_content = """Generate three very brief follow-up questions that the user would likely ask next about the annual reports.
Use double angle brackets to reference the questions, e.g. <<What strategies should Unilever consider to continue growing its turnover?>>.
Try not to repeat questions that have already been asked.
Only generate questions and do not generate any text before or after the questions. Preface the follow-up questions with 'Next Questions:'"""

    query_prompt_template = """Below is a history of the conversation so far, and a new question asked by the user that needs to be answered by searching in a knowledge base about the annual reports of Unilever and its competitors. 
Generate a new search query based on the conversation and the new question. The search query, when entered into Azure Cognitive Search using the Semantic Search method, should be able to generate a coherent answer based on the original user question.
Do not include cited source filenames and document names e.g info.txt or doc.pdf in the search query terms.
Do not include any text inside [] or <<>> in the search query terms.
Do not include any special characters like '+'.
If the question is not in English, translate the question to English before generating the search query.
If you cannot generate a search query, return just the number 0.
If the year is not specified, add "at least 5 years" to the search query. 
If the company is not specified, specify that the search query is about "Unilever and its top 3 competitors". 
Understand what the user is looking for and add related areas of analysis to the search query.
"""
    query_prompt_few_shots = [
        {'role' : USER, 'content' : "What is Unilever's sales?"},
        {'role' : ASSISTANT, 'content' : "Unilever's Sales KPIs for the year 2021" },
        {'role' : USER, 'content' : "What is P&G's sales for 2021?"},
        {'role' : ASSISTANT, 'content' : "P&G's turnover in 2021" },
        {'role' : USER, 'content' : "What is the breakdown of turnover by Business Group?"},
        {'role' : ASSISTANT, 'content' : "Components of the turnover of Unilever in 2021 by Business Group"},
        {'role': USER, 'content': "What is Unilever's sales for 2015-2019?"},
        {'role': ASSISTANT, 'content':"Unilever's financial performance from 2015 to 2019"}
      
    ]

    def __init__(self, search_client: SearchClient, chatgpt_deployment: str, chatgpt_model: str, embedding_deployment: str, sourcepage_field: str, content_field: str):
        self.search_client = search_client
        self.chatgpt_deployment = chatgpt_deployment
        self.chatgpt_model = chatgpt_model
        self.embedding_deployment = embedding_deployment
        self.sourcepage_field = sourcepage_field
        self.content_field = content_field
        self.chatgpt_token_limit = get_token_limit(chatgpt_model)

    async def run(self, history: list[dict[str, str]], overrides: dict[str, Any]) -> Any:
        has_text = overrides.get("retrieval_mode") in ["text", "hybrid", None]
        has_vector = False #overrides.get("retrieval_mode") in ["vectors", "hybrid", None]
        use_semantic_captions = True if overrides.get("semantic_captions") and has_text else False
        top = overrides.get("top") or 3
        # exclude_category = overrides.get("exclude_category") or None
        # filter = "category ne '{}'".format(exclude_category.replace("'", "''")) if exclude_category else None

        user_q = 'Generate search query for: ' + history[-1]["user"]

        # STEP 1: Generate an optimized keyword search query based on the chat history and the last question
        messages = self.get_messages_from_history(
            self.query_prompt_template,
            self.chatgpt_model,
            history,
            user_q,
            self.query_prompt_few_shots,
            self.chatgpt_token_limit - len(user_q)
            )

        chat_completion = await openai.ChatCompletion.acreate(
            deployment_id=self.chatgpt_deployment,
            model=self.chatgpt_model,
            messages=messages,
            temperature=0.5,
            max_tokens=6000,
            n=1)

        query_text = chat_completion.choices[0].message.content
        query_text = query_text.replace('\"',"")
        if query_text.strip() == "0":
            query_text = history[-1]["user"] # Use the last user input if we failed to generate a better query

        # STEP 2: Retrieve relevant documents from the search index with the GPT optimized query

        # If retrieval mode includes vectors, compute an embedding for the query
        # if has_vector:
        #     query_vector = (await openai.Embedding.acreate(engine=self.embedding_deployment, input=query_text))["data"][0]["embedding"]
        # else:
        #     query_vector = None

        #  # Only keep the text query if the retrieval mode uses text, otherwise drop it
        # if not has_text:
        #     query_text = None

        # Use semantic L2 reranker if requested and if retrieval mode is text or hybrid (vectors + text)
        if overrides.get("semantic_ranker") and has_text:
            r = self.search_client.search(query_text,
                                        #   filter=filter,
                                          query_type=QueryType.SEMANTIC,
                                          query_language="en-us",
                                          query_speller="lexicon",
                                          semantic_configuration_name="default",
                                          top=top,
                                          query_caption="extractive|highlight-false" if use_semantic_captions else None
                                        #   vector=query_vector,
                                        #   top_k=50 if query_vector else None,
                                        #   vector_fields="embedding" if query_vector else None
                                        )
        else:
            r = self.search_client.search(query_text,
                                        #   filter=filter,
                                          top=top)
                                          # vector=None, #query_vector
                                          # top_k=None, #50 if query_vector else None,
                                          # vector_fields=None) #"embedding" if query_vector else None)
        if use_semantic_captions:
            # print(dir(doc) for doc in r)
            results = [doc[self.sourcepage_field] + ": " + nonewlines(" . ".join([c.text for c in doc['@search.captions']])) for doc in r]
        else:
            results = [doc[self.sourcepage_field] + ": " + nonewlines(doc[self.content_field]) for doc in r]
        content = "\n".join(results)

        follow_up_questions_prompt = self.follow_up_questions_prompt_content if overrides.get("suggest_followup_questions") else ""

        # STEP 3: Generate a contextual and content specific answer using the search results and chat history

        # Allow client to replace the entire prompt, or to inject into the exiting prompt using >>>
        prompt_override = overrides.get("prompt_override")
        if prompt_override is None:
            system_message = self.system_message_chat_conversation.format(injected_prompt="", follow_up_questions_prompt=follow_up_questions_prompt)
        elif prompt_override.startswith(">>>"):
            system_message = self.system_message_chat_conversation.format(injected_prompt=prompt_override[3:] + "\n", follow_up_questions_prompt=follow_up_questions_prompt)
        else:
            system_message = prompt_override.format(follow_up_questions_prompt=follow_up_questions_prompt)

        messages = self.get_messages_from_history(
            system_message,
            self.chatgpt_model,
            history,
            history[-1]["user"]+ "\n\nSources:\n" + content, # Model does not handle lengthy system messages well. Moving sources to latest user conversation to solve follow up questions prompt.
            max_tokens=self.chatgpt_token_limit)

        chat_completion = await openai.ChatCompletion.acreate(
            deployment_id=self.chatgpt_deployment,
            model=self.chatgpt_model,
            messages=messages,
            temperature=overrides.get("temperature") or 0.35,
            max_tokens=8000,
            n=1)

        chat_content = chat_completion.choices[0].message.content
        msg_to_display = '\n\n'.join([str(message) for message in messages])
        chat_content_split = chat_content.split("Next Questions:", 1)
        sources = [s.split(":")[0] for s in results]
        end = {"data_points": results, "answer": chat_content_split[0], "sources": sources, "questions": [q for q in chat_content_split[1].split('?')], "thoughts": f"Searched for:<br>{query_text}<br><br>Conversations:<br>" + msg_to_display.replace('\n', '<br>')}
        # print('Original Question', history[-1]["user"], '==============')
        # print('Refined Question:', query_text, '==============')
        # print('Answer:', end['answer'], '==============')
        # print('Dictionary Keys:',end.keys(),'==============')
        # print('Data Points:', results)
        return end

    def get_messages_from_history(self, system_prompt: str, model_id: str, history: list[dict[str, str]], user_conv: str, few_shots = [], max_tokens: int = 4096) -> list:
        message_builder = MessageBuilder(system_prompt, model_id)

        # Add examples to show the chat what responses we want. It will try to mimic any responses and make sure they match the rules laid out in the system message.
        for shot in few_shots:
            message_builder.append_message(shot.get('role'), shot.get('content'))

        user_content = user_conv
        append_index = len(few_shots) + 1

        message_builder.append_message(self.USER, user_content, index=append_index)

        for h in reversed(history[:-1]):
            if bot_msg := h.get("bot"):
                message_builder.append_message(self.ASSISTANT, bot_msg, index=append_index)
            if user_msg := h.get("user"):
                message_builder.append_message(self.USER, user_msg, index=append_index)
            if message_builder.token_length > max_tokens:
                break

        messages = message_builder.messages
        return messages
