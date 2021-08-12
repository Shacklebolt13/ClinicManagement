from django.http import HttpResponse,HttpRequest
from django.http.response import Http404
from django.shortcuts import redirect, render
from authentication import models
from datetime import datetime
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
    if(request.method.upper()!='POST'):
        return Http404()
    doc : models.Practitioner
    doc=request.POST.get('docid',False)
    doc=models.Practitioner.objects.filter(creds_id=int(doc))[0]
    params={'id':doc.creds.id,
        'name':doc.creds.first_name+doc.creds.last_name,
            'price':doc.price,
            'windowo':doc.available.fromt,
            'windowc':doc.available.to}
    return render(request,'fullsite/book.html',params)
    

def seeApps(request:HttpRequest):
    params={}
    user=request.COOKIES.get('user',False)
    user=models.Practitioner.objects.get(creds_id=int(user))
    bookings=user.booking_set.values()
    if(len(bookings)==0):
        params['msg']='NO Bookings Available'
    else:
        bookinglist=[]
        for i in bookings:
            if(i['paid']):    
                booking=i
                booking['date']=str(booking['date'])
                vis=models.Booking.objects.get(id=i['id']).visitor.values()[0]['id']
                vis=models.Visitor.objects.get(id=vis)
                booking['name']=vis.creds.first_name+" "+vis.creds.last_name
                bookinglist.append(booking)
        params['bookings']=bookinglist
        print(params)
    return render(request,'fullsite/seeApps.html',params)


def pay(request:HttpRequest):
    if(request.method.upper()!='POST'):
        return Http404()
    doc=request.POST.get('docid',False)
    date=request.POST.get('date',False)
    user=request.COOKIES.get('user',False)
    user=models.Visitor.objects.filter(creds_id=int(user))[0]
    print(user.is_verified)
    if(not user.is_verified):
        return redirect('confirm')
    try:
        booking=models.Booking.objects.filter(visitor=user)[0]
    except Exception:
        booking=models.Booking(date=datetime.strptime(date,'%Y-%m-%d'))
        practitioner=models.Practitioner.objects.get(creds_id=int(doc))
        booking.save()
        booking.practitioner.add(practitioner)
        booking.visitor.add(user)
        booking.save()
        

    params={'bookId':booking.id}
    return render(request,'fullsite/pay.html',params)


def paydone(request:HttpRequest):
    if(request.method.upper()!='POST'):
        return Http404()
    
    bookid=request.POST.get('bookid',False)
    book=models.Booking.objects.get(id=bookid)
    book: models.Booking
    book.paid=True
    book.save()
    return HttpResponse("""Your payment has been completed and an appointment has been booked. 
    Check your Email and SMS for Confirmation. Kindly bring an ID proof and The sent confirmation for the appointment. 
    <a href="home">Click here to go to home </a>""")



