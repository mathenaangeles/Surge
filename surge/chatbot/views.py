from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from django.shortcuts import render, redirect
import environ
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import openai
import os
from typing import List
from utils import ChatReadRetrieveReadApproach

env = environ.Env()
environ.Env.read_env()

openai.api_type = env["AZURE_OPENAI_TYPE"]
openai.api_base = env["AZURE_OPENAI_SERVICE"]
openai.api_version = env["AZURE_OPENAI_CHATGPT_MODEL"]
openai_chatgpt_model = env["AZURE_OPENAI_CHATGPT_MODEL"]
openai.api_type = env["AZURE_OPENAI_TYPE"]
openai.api_key = env["OPENAI_SECRET_KEY"]
openai_chatgpt_deployment = os.environ["AZURE_OPENAI_CHATGPT_DEPLOYMENT"]

azure_search_service = env["AZURE_SEARCH_SERVICE"]
azure_search_index = env["AZURE_SEARCH_INDEX"]
azure_secret_key = AzureKeyCredential(env["AZURE_SECRET_KEY"])


search_client = SearchClient(endpoint=azure_search_service,
                             index_name=azure_search_index,
                             credential=azure_secret_key)

ChatReadRetrieveReadApproach(search_client,openai_chatgpt_model,openai_chatgpt_model) # the ChatGPT Method from utils.py

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