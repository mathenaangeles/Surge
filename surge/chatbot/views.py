from django.shortcuts import render, redirect
import openai

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

openai.api_key = env('API_KEY')

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