from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# localhost:8000/demo/hello

def say_hello(request):
    return render(request, 'index.html', {"name": ""})


def welcome(request, name):
    return HttpResponse(f"Hello {name}")
