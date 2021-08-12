from rest_framework import serializers
from . import models

class CredSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.User
        fields=['first_name','last_name','email']

class PracSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Practitioner
        fields = "__all__"


class VisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = "__all__"



class AddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = "__all__"


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Slot
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BankAccount
        fields = ["pan","acc","ifsc"]