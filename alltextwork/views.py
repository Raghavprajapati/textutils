from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request ,'index.htm')

def about(request):
    return HttpResponse('about RAGHAV')
def anylazie(request):
    #get the text
    djtext  = request.POST.get('text','default')
    
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    newlineremover = request.POST.get('newlineremover','off')
    
    if removepunc == "on":
        puncuations = '''~`!@#$%^&*()_-}[]{\|:;"'<,>.?/'''
        anaylzed =""
        for char in djtext:
            if char not in puncuations:
                anaylzed = anaylzed+char
        params = {'purpuse':'Removed Puncuatations','analyzed_text':anaylzed}
        djtext = anaylzed
        

    if(uppercase =="on"):
        anaylzed = ""
        for char in djtext:
            anaylzed = anaylzed + char.upper()
        params = {'purpuse':'Channge to upper case ','analyzed_text':anaylzed}
        djtext = anaylzed
        
    if(newlineremover=="on"):
        anaylzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                anaylzed = anaylzed + char
            params = {'purpuse':'New line remover ','analyzed_text':anaylzed}
    
    if(removepunc!="on" and uppercase!="on"and newlineremover!="on"):
        return HttpResponse("Error")

    
    return render(request ,'anylize.htm',params)