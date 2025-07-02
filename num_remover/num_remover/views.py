from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def rmv(request):
    textarea = request.GET.get('textarea', '')
    numbers = '0123456789'
    analyzed = ''
    for char in textarea:
        if char not in numbers:
            analyzed = analyzed+char

    params = {'original_text': textarea, 'analyzed_text': analyzed}
    return render(request,'index.html' ,params)

def about(request):
    return render(request, 'about.html')

