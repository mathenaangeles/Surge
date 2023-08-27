import asyncio
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import openai
import os
from typing import List
from utils import ChatReadRetrieveReadApproach

openai.api_type = os.environ["AZURE_OPENAI_TYPE"]
openai.api_base = os.environ["AZURE_OPENAI_SERVICE"]
openai.api_version = os.environ["AZURE_OPENAI_CHATGPT_VERSION"]
openai_chatgpt_model = os.environ["AZURE_OPENAI_CHATGPT_MODEL"]
openai.api_type = os.environ["AZURE_OPENAI_TYPE"]
openai.api_key = os.environ["OPENAI_SECRET_KEY"]
openai_chatgpt_deployment = os.environ["AZURE_OPENAI_CHATGPT_DEPLOYMENT"]

azure_search_service = os.environ["AZURE_SEARCH_SERVICE"]
azure_search_index = os.environ["AZURE_SEARCH_INDEX"]
azure_secret_key = AzureKeyCredential(os.environ["AZURE_SECRET_KEY"])


search_client = SearchClient(endpoint=azure_search_service,
                             index_name=azure_search_index,
                             credential=azure_secret_key)

# input
history = [{"user": "Unilever background"}]

# settings
overrides = {"retrieval_mode": "text", "semantic_ranker": False, "semantic_captions": False, "top": 3, "suggest_followup_questions": True}

# Instantiate GPT
agent = ChatReadRetrieveReadApproach(
                                    search_client,
                                    openai_chatgpt_deployment,
                                    openai_chatgpt_model,
                                    'chat','sourcepage','content') 

# Run
async def test():
  await agent.run(history,overrides)
asyncio.run(test())

def home(request):
    try:
        if 'messages' not in request.session:
            request.session['messages'] = [
                {"role": "system", "content": "Return a clear and concise answers."},
            ]
        if request.method == 'POST':
            prompt = request.POST.get('prompt')
            temperature = float(request.POST.get('temperature', 0.1))
            request.session['messages'].append({"role": "user", "content": prompt})
            request.session.modified = True
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=request.session['messages'],
                temperature=temperature,
                max_tokens=1000,
            )
            formatted_response = response['choices'][0]['message']['content']
            request.session['messages'].append({"role": "system", "content": formatted_response})
            request.session.modified = True
            context = {
                'messages': request.session['messages'],
                'prompt': '',
                'temperature': temperature,
            }
            return render(request, context)
        else:
            context = {
                'messages': request.session['messages'],
                'prompt': '',
                'temperature': 0.1,
            }
            return render(request, context)
    except Exception as e:
        print(e)
        return redirect('error')

def error_handler(request):
    return render(request)