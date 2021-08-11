from django.http import HttpResponse,HttpRequest
from django.shortcuts import render

# Create your views here.
def home(request: HttpRequest):
    return HttpResponse('this is logged home')