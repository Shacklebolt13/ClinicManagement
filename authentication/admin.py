from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Practitioner)
admin.site.register(models.Visitor)
admin.site.register(models.Address)
admin.site.register(models.BankAccount)
admin.site.register(models.Slot)
admin.site.register(models.Booking)