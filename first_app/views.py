from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse

def index(request):
    # Create a large list to increase RAM usage
    large_list = []
    for i in range(100000):
        large_list.append("hello world" * 1000)  # Create a large string and append to the list

    total_length = sum(len(s) for s in large_list)
    

    return HttpResponse(f'HHM.....Hello World! This is CN Django Test.By - Harsh Kanani aa.....web hooks test harsh kanani webhook testing 123456789 hello hi. Total length of strings: {total_length}')
