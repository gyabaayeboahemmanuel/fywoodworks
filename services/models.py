from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model
from accounts.models import Staff

User = get_user_model()
LOG_CHOICES = (
    ("2 X 4", "2 X 4"),
    ("2 X 6", "2 X 6"),
    ("2 X 8", "2 X 8"),
    ("2 X 2", "2 X 2"),
    ("1 X 9", "1 X 9"),
    ("1 X 10", "1 X 10"),
    ("1 X 12", "1 X 12"),
    ("Wawa Board", "Wawa Board"),
    ("Nyamedua","Nyamedua"),
    ("Saba", "Saba"),
    ("Ceiling Buttons", "Ceiling Buttons"),
    
)

MACHINE_WORK_CHOICES = (
     ("Planning", "Planning"),
     ("Saw","Saw"),
     ("Ripping", "Ripping"),
)
# class Operator (models.Model): 
#     user = models.ForeignKey(User, on_delete= models.CASCADE)
#     name = models.CharField(max_length=100)
#     hometown = models.CharField(max_length=100)
#     phonenumber= models.CharField(max_length=10)

#     def __str__(self):
#         return self.name

# Operator Models.
class Operator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hometown = models.CharField(max_length=50)
    phone_number= models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ("-first_name",)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
        
# Models for Works
class MachineWork (models.Model):
    machine_work_type = models.CharField(choices=MACHINE_WORK_CHOICES, max_length=30)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    date_recorded = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.description
    def was_entered_today(self):
        return self.entry_date >= self.entry_date - datetime.timedelta

    # class Meta:
    #     ordering = ("-user",)

class WoodFromBush(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    woodtype = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=9 )
    processed = models.BooleanField(default=False)
    date_purchased = models.DateTimeField(auto_now_add= True)

class Log(models.Model):
    wood_from_bush = models.ForeignKey(WoodFromBush, on_delete=models.CASCADE)
    log_type = models.CharField(choices=LOG_CHOICES, max_length=30)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits= 9)


class WoodSale(models.Model):
    log = models.ForeignKey(Log, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits= 9, null=True, blank=True)
    date_sold = models.DateTimeField(auto_now_add= True)
    

class Salary(models.Model):
    staff = models.ForeignKey(Staff, on_delete=CASCADE)
    amount_paid = models.IntegerField()
    date_paid = models.DateTimeField(auto_now_add= True)

class GeneralExpence(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    date_recorded = models.DateTimeField(auto_now_add= True)


class FurnitureInventory (models.Model):
    item_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null= True, blank=True)
    unit_price = models.DecimalField(decimal_places=2, max_digits=9)
    unit_expenses_on_work = models.DecimalField(decimal_places=2, max_digits=9)
    quantity = models.IntegerField()
    date_made = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.item_name + " " + str(self.quantity)

class FurnitureSale (models.Model):
    furnitureInventory = models.ForeignKey(FurnitureInventory, on_delete=CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=9)
    date_sold = models.DateTimeField(auto_now_add= True)

    def save(self, *args, **kwargs) -> None:
        if self.furnitureInventory.quantity > self.quantity:
            self.furnitureInventory.quantity = self.furnitureInventory.quantity - self.quantity
            self.total_price = self.quantity * self.furnitureInventory.unit_price
        super(FurnitureSale, self).save(*args, **kwargs)

