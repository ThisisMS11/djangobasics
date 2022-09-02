from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'Mohit Saini', 'place':'Mars'}
    return render(request, 'index.html', params)

def capfirst(request):
    return HttpResponse("captilize the first letter of the word")