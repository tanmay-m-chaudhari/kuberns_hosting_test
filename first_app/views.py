from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello World! This is CN Django Test. will be rocking soon in industry.')