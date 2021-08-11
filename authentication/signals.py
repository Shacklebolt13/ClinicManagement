from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
from . import models
from datetime import date

@receiver(post_save,sender=User)
def create(sender,instance: User,created,**kwargs):
    if(len(instance.groups.all())>0):
        #print(instance.groups.all()[0] )
        
        if(str(instance.groups.all()[0]) == 'Practitioners'):
            try:
                instance.practitioner
            except Exception:
                slot=models.Slot(fromt='00:00',to='23:00')
                slot.save()
                ba=models.BankAccount(acc=0)
                ba.save()
                models.Practitioner(
                    creds=instance,
                    dp="",
                    phone=0,
                    available=slot,
                    bank=ba).save()
        else:
            try:
                instance.visitor
            except Exception:
                ad=models.Address(postal=0 )
                ad.save()
                models.Visitor(
                    creds=instance,
                    nationality='',
                    dob=date.today().strftime('%Y-%m-%d'),
                    gender='',
                    add=ad).save()