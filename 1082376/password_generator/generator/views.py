from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    HttpResponse("Hello, you are here")