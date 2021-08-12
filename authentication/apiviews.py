from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers


class Pracs(APIView):

    def get(self,request):
        pracs=models.Practitioner.objects.all()

        prac_ser=serializers.PracSerializer(pracs,many=True)
        return Response(prac_ser.data)

    def post(self,request):
        pass


class Vis(APIView):

    def get(self,request):
        vis=models.Visitor.objects.all()
        vis_ser=serializers.VisSerializer(vis,many=True)
        return Response(vis_ser.data)

    def post(self,request):
        pass


class Creds(APIView):

    def get(self,request):
        creds=models.User.objects.all()
        creds_ser=serializers.CredSerializer(creds,many=True)
        return Response(creds_ser.data)

    def post(self,request):
        pass