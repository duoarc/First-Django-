from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    #text = """<h1>Welcome to my First App!</h1>"""
    return render(request, "C:\Users\User pc\Documents\Coding\Development\index.html", {})
    #return HttpResponse(text)
# Create your views here.
