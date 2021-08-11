from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def signin(request :HttpRequest):
    params={}
    return render(request,'authentication/signin.html',params)

def signup(request: HttpRequest):
    params={}
    return render(request,'authentication/signup.html',params)

def pracSignin(request: HttpRequest):
    params={}
    return render(request,'authentication/pracSignin.html',params)


def price(request: HttpRequest):
    params={}
    return render(request,'authentication/price.html',params)