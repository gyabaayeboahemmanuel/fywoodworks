from django.db import models
from django.utils import timezone
import datetime


# Models For people

class Operator (models.Model): 
    name = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)
    phonenumber= models.CharField(max_length=10)

    def __str__(self):
        return self.name
class Staff(models.Model):
    surname = models.CharField(max_length=100)
    otherNames = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)
    phoneNumber= models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    picture = models.ImageField()

    def __str__(self) -> str:
        return self.surname + " " + self.otherNames

 

# Models for Works
class MachineWork (models.Model):
    description = models.CharField(max_length=200)
    entry_date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.description
    def was_entered_today(self):
        return self.entry_date >= timezone.now() - datetime.timedelta

class Capentry(models.Model):
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=200)
    unit_price = models.DecimalField(decimal_places=2, max_digits=9)
    quantity = models.IntegerField()
    expenses = models.DecimalField(decimal_places=2, max_digits=9)

class WoodFromBush(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    woodtype = models.CharField(max_length=200)
    quantity = models.IntegerField()


class WoodWork(models.Model):
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=200)
    unit_price = models.DecimalField(decimal_places=2, max_digits=9)
    quantity = models.IntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=9)


