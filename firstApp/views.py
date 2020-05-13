from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def display(request):
    return HttpResponse("<h1>My First Django APP!!</h1>")
