from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib.auth import authenticate
from . import models
from datetime import date, datetime
# Create your views here.


def signout(request :HttpRequest):
    resp=redirect("home")
    resp.delete_cookie('user')
    return resp

def signin(request :HttpRequest):
    params={}
    if('user' in request.COOKIES):
        return redirect('home')

    if(request.method.upper()!='POST'):
        print('no post')
        return render(request,'authentication/signin.html',params)

    email=request.POST.get('email',False)
    password=request.POST.get('password',False)

    user=authenticate(username=email,password=password)
    print(user)
    if(user is not None):
        resp=redirect('home')
        resp.set_cookie('user',user.id)
        return resp
    else:
        params['error']="wrong credentials"
    return render(request,'authentication/signin.html',params)

    

def signup(request: HttpRequest):
    params={}
    if(request.method.upper()!="POST"):
        return render(request,'authentication/signup.html',params)  
    
    uname=request.POST.get('username',False)
    password=request.POST.get('password',False)
    gender=request.POST.get('gender',False)
    email=request.POST.get('email',False)
    nat=request.POST.get('nat',False)
    dob=request.POST.get('dob',False)
    addr1=request.POST.get('addr1',False)
    addr2=request.POST.get('addr2',False)
    city=request.POST.get('city',False)
    state=request.POST.get('state',False)
    postal=request.POST.get('postal',False)
    country=request.POST.get('country',False)
    dob=datetime.strptime(dob,'%Y-%m-%d').date()
    user=models.User.objects.create_user(email,email,password)
    user.first_name=uname
    vis=models.Visitor(creds=user,nationality=nat,gender=gender,dob=dob)
    vis.save()
    add=models.Address(addr1=addr1,addr2=addr2,postal=int(postal),city=city,state=state,country=country,vis=vis)
    add.save()
    
    resp=redirect('home')
    resp.set_cookie(key='user',value=vis.creds.id)

    return resp

        

def pracSignin(request: HttpRequest):
    params={}
    return render(request,'authentication/pracSignin.html',params)


def price(request: HttpRequest):
    params={}
    return render(request,'authentication/price.html',params)