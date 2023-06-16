from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Har Har Mahadev.....Hello World! This is CN Django Test.By - Harsh Kanani .....web hook test')