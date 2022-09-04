from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def capfirst(request):
    return HttpResponse("captilize the first letter of the word")


def analyze(request):
    content = request.GET.get('content', 'default text')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    removenewline = request.GET.get('removenewline', 'off')
    RemoveExtraSpaces = request.GET.get('RemoveExtraSpaces', 'off')

    analyzed = content
    count=0

    if (removepunc == 'on'):
        holdstring = analyzed
        analyzed=''
        punctuations = '''!()-[]{};:'"`\,<>./?@#$%^&*_~'''
        for char in holdstring:
            if char not in punctuations:
                analyzed = analyzed+char

    if (fullcaps == 'on'):
        holdstring = analyzed
        analyzed = ''
        for char in holdstring:
            analyzed = analyzed + char.upper()
                
    if (removenewline == 'on'):
        holdstring = analyzed
        analyzed = ''
        for char in holdstring:
            if (char != '\n'):
                analyzed = analyzed+char

    if(RemoveExtraSpaces=='on'):
        holdstring = analyzed
        analyzed = ''
        for index, char in enumerate(holdstring):
            if not(holdstring[index]==' ' and holdstring[index+1]==' '):
                analyzed=analyzed+char

    for char in analyzed:
        if(char!=' '):
            count+=1

        
        


    

    print('finally analyzed : ', analyzed)
    params = {'analyzed_text': analyzed , 'charcount':count}

    return render(request, 'analyze.html', params)
