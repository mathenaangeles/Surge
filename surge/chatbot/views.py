import asyncio
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .serializers import HistorySerializer
from .models import History
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import openai
import os
from typing import List
from .utils import ChatReadRetrieveReadApproach

from asgiref.sync import async_to_sync, sync_to_async

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
# settings
overrides = {"retrieval_mode": "text", 
             "semantic_ranker": True, 
             "semantic_captions": True, 
             "top": 3, 
             "suggest_followup_questions": True,
             "temperature": 0.35}

# Instantiate GPT
agent = ChatReadRetrieveReadApproach(
                                    search_client,
                                    openai_chatgpt_deployment,
                                    openai_chatgpt_model,
                                    'chat','sourcepage','content') 

# Run
async def chatbot(history):
  return await agent.run(history, overrides)

@csrf_exempt
def histories(request):
    if(request.method == 'GET'):
        histories =  History.objects.all()
        serializer = HistorySerializer(histories, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = HistorySerializer(data=data)
        if(serializer.is_valid()):
            conversations = [*History.objects.values_list('conversation', flat=True)]
            result = asyncio.run(chatbot(conversations + [data['conversation']]))
            data['conversation']['bot'] = result['answer']
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def error_handler(request):
    return render(request)