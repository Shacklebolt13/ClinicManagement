from authentication import models
from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def home(request :HttpRequest):
    if('user' in request.COOKIES):
        user=request.COOKIES.get('user',False)
        user=models.User.objects.get(id=int(user))
        try:
            user.practitioner
            return redirect('appis')
        except Exception:
            if(models.Visitor.objects.get(creds=user).is_verified):
                return redirect('site')
            else:
                return redirect('confirm')
    else:
        return redirect('signin')
