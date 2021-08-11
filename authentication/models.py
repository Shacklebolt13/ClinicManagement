from typing import Text
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Address(models.Model):
    addr1=models.TextField(blank=True)
    addr2=models.TextField(blank=True)
    postal=models.IntegerField(blank=True)
    city=models.TextField(blank=True)
    state=models.TextField(blank=True)
    country=models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.visitor.creds.first_name} {self.visitor.creds.last_name} ({self.visitor.creds.username}) 's Address "





class BankAccount(models.Model):
    pan=models.TextField(blank=True,max_length=12)
    acc=models.IntegerField(blank=True)
    ifsc=models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.practitioner.creds.first_name} {self.practitioner.creds.last_name} ({self.practitioner.creds.username}) 's Bank "




class Slot(models.Model):
    fromt=models.TimeField(blank=True)
    to=models.TimeField(blank=True)

    def __str__(self) -> str:
        return f"{self.practitioner.creds.first_name} {self.practitioner.creds.last_name} ({self.practitioner.creds.username}) 's SLOT"




class Practitioner(models.Model):
    creds=models.OneToOneField(User,on_delete=models.CASCADE)
    dp=models.ImageField(blank=True,upload_to="media")
    phone=models.IntegerField(blank=True)
    available=models.OneToOneField(Slot,blank=True,on_delete=models.RESTRICT)
    bank=models.OneToOneField(BankAccount,blank=True,on_delete=models.RESTRICT)
    duration_in_mins=models.IntegerField()
    price=models.IntegerField(default=500)
    

    def __str__(self) -> str:
        return f"{self.creds.first_name} {self.creds.last_name} ({self.creds.username})"




class Visitor(models.Model):    
    creds=models.OneToOneField(User,on_delete=models.CASCADE)
    nationality=models.TextField(blank=False)
    gender=models.TextField(blank=False)
    dob=models.DateField(blank=False)
    type=models.BooleanField(default=False) #False - visitor, True - Patient
    add=models.OneToOneField(Address,on_delete=models.RESTRICT)
    
    expectedOTP=models.TextField(blank=True)
    is_verified=models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.creds.first_name} {self.creds.last_name} ({self.creds.username})"





class Booking():
    practitioner=models.ManyToManyField(Practitioner)
    visitor=models.OneToOneField(Visitor,on_delete=models.CASCADE)
    timing=models.OneToOneField(Slot,on_delete=models.CASCADE)
    date=models.DateField()
    



