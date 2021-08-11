from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from authentication import models

# Create your views here.
def home(request: HttpRequest):
    pracs=models.Practitioner.objects.all()
    params={'pracs':[]}
    for i in pracs:
        prac={}
        prac['id']=i.creds.id
        prac['name']=i.creds.first_name+" "+i.creds.last_name
        prac['img']="/"+str(i.dp)
        prac['duration']=i.duration_in_mins
        prac['price']=i.price
        prac['tslotf']=str(i.available.fromt)
        prac['tslott']=str(i.available.to)
        params['pracs'].append(prac)
        del prac
    
    return render(request,'fullsite/bookDoc.html',params)

def book(request : HttpRequest):
    return HttpResponse('booking page under cons')