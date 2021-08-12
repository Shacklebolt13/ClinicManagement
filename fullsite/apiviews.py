from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication import models
from authentication import serializers

class Appointment(APIView):
    def get(self,request: HttpRequest):
        id=int(request.GET.get('id',False))
        user= models.Practitioner.objects.filter(creds_id=id) 
        print(user)
        if(len(user)>0):
            user=user[0]
        else:
            user=models.Visitor.objects.filter(creds_id=id)
            if(len(user)>0):
                user=user[0] 
            else:
                user=None
        if(user is not None):
            print(user) 
            bookings=user.booking_set.values()
            tot=[]
            for booking in bookings:
                B=models.Booking.objects.get(id=booking['id']) 
                data=serializers.BookSerializer(B).data
                data['practitioner']=serializers.PracSerializer(models.Practitioner.objects.get(id=data['practitioner'][0])).data
                data['visitor']=serializers.VisSerializer(models.Visitor.objects.get(id=data['visitor'][0])).data
                tot.append(data)
                del B
                del data
            return Response(tot)
        else:
            return HttpResponse("Wrong Syntax")


