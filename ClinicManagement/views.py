from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def home(request :HttpRequest):
    if('user' in request.COOKIES):
        return redirect('site')
    else:
        return redirect('signin')
