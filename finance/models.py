from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class MachineWork (models.Model):
    description = models.CharField(max_length=200)
    entry_date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.description
    def was_entered_today(self):
        return self.entry_date >= timezone.now() - datetime.timedelta

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
 