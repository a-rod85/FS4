from django.shortcuts import render, HttpResponse

# Create your views here.
def say_Hello(request):
    return HTTPResponse("Hello!")