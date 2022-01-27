from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model
from accounts.models import Staff

User = get_user_model()
WOOD_FROM_BUSH_CHOICES = (
    ("2 X 8 - Red Wood", "2 X 8 - Red Wood"),
    ("2 X 8 - Ky3nky3n", "2 X 8 - Ky3nky3n"),
    ("2 X 8 - Oframe", "2 X 8 - Oframe"),
    ("2 X 8 - Odum", "2 X 8 - Odum"),
    ("2 X 8 - Saiba", "2 X 8 - Saiba"),
    ("2 X 8 - Wawa", "2 X 8- Wawa"),
    ("2 X 6 - Red Wood", "2 X 6 - Red Wood"),
    ("2 X 6 - Ky3nky3n", "2 X 6 - Ky3nky3n"),
    ("2 X 6 - Oframe", "2 X 6 - Oframe"),
    ("2 X 6 - Odum", "2 X 6 - Odum"),
    ("2 X 6 - Saiba", "2 X 6 - Saiba"),
    ("2 X 6 - Wawa", "2 X 6- Wawa"),
    ("1 X 9 - Ky3nky3n", "1 X 9 - Ky3nky3n"),
    ("1 X 9 - Red Wood", "1 X 9 - Red Wood"),
    ("1 X 9 - Oframe", "1 X 9 - Oframe"),
    ("1 X 9 - Odum", "1 X 9 - Odum"),
    ("1 X 9 - Saiba", "1 X 9 - Saiba"),
    ("1 X 9 - Wawa", "1 X 9- Wawa"),
    ("1 X 10 - Ky3nky3n", "1 X 10 - Ky3nky3n"),
    ("1 X 10 - Red Wood", "1 X 10 - Red Wood"),
    ("1 X 10 - Oframe", "1 X 10 - Oframe"),
    ("1 X 10 - Odum", "1 X 10 - Odum"),
    ("1 X 10 - Saiba", "1 X 10 - Saiba"),
    ("1 X 10 - Wawa", "1 X 10- Wawa"),
    ("1 X 12 - Ky3nky3n", "1 X 12 - Ky3nky3n"),
    ("1 X 12 - Red Wood", "1 X 12 - Red Wood"),
    ("1 X 12 - Oframe", "1 X 12 - Oframe"),
    ("1 X 12 - Odum", "1 X 12 - Odum"),
    ("1 X 12 - Saiba", "1 X 12 - Saiba"),
    ("1 X 12 - Wawa", "1 X 12- Wawa"),
    ("Ceiling Buttons", "Ceiling Buttons"),
    
)

MACHINE_WORK_CHOICES = (
     ("Planing", "Planing"),
     ("Saw","Saw"),
     ("Ripping 1X12 Board", "Ripping 1X12 Boards"),
     ("2X6 & 2X8 wood", "2X6 & 2X8 wood"),
     ("Beam 3X12", "Beam 3X12"),
     ("Beam 4X12", "Beam 4X12"),
     ("Wabire & Asemfra", "Wabire & Asemfra"),
     ("Bed Machine", "Bed Machine"),
     ("Door", "Door"),
     ("Door Gate", "Door Gate"),
     ("Ban-Saw", "Ban-Saw"),
     ("Mono Desk", "Mono Desk"),
     ("Door and Cramping", "Door and Cramping"),
     ("Frame Plaining 3 in 1", "Frame Plaining 3 in 1"),
     ("2 in 1 & Door Frame", "2 in 1 & Door Frame"),

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
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    date_recorded = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.machine_work_type
    def was_entered_today(self):
        return self.entry_date >= self.entry_date - datetime.timedelta

    # class Meta:
    #     ordering = ("-user",)

class WoodFromBush(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
   # woodtype = models.CharField(max_length=200)
    description = models.CharField(choices =WOOD_FROM_BUSH_CHOICES, max_length=30 )
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=9 )
    sell_price = models.DecimalField(decimal_places=2, max_digits=9 )
    date_purchased = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.description + " || " + str(self.quantity)

# class Log(models.Model):
#     wood_from_bush = models.ForeignKey(WoodFromBush, on_delete=models.CASCADE)
#     log_type = models.CharField(choices=LOG_CHOICES, max_length=30)
#     quantity = models.IntegerField()
#     unit_price = models.DecimalField(decimal_places=2, max_digits= 9)


class WoodSale(models.Model):
    # customer = models.CharField(max_length = 100)
    total_price = models.DecimalField(decimal_places=2, max_digits= 9, default=0.0)
    date_sold = models.DateTimeField(auto_now_add= True)
    # def __str__(self):
    #     return self.total_price

class WoodItemSale(models.Model):
    woodfrombush = models.ForeignKey(WoodFromBush, on_delete= models.CASCADE)
    woodsale = models.ForeignKey(WoodSale, verbose_name=("woodsale"), on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(decimal_places=2, max_digits=9)
  
    def __str__(self):
        return self.woodfrombush.description

    def save (self, *args, **kwargs):
        self.woodfrombush.quantity = int(self.woodfrombush.quantity)- int(self.quantity)
        self.woodfrombush.save()
        super(WoodItemSale, self).save(*args, **kwargs)

class Salary(models.Model):
    staff = models.ForeignKey(Staff, on_delete=CASCADE)
    amount_paid = models.DecimalField(decimal_places=2, max_digits= 9)
    date_paid = models.DateTimeField(auto_now_add= True)

class GeneralExpence(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    date_recorded = models.DateTimeField(auto_now_add= True)

class FurnitureInventory (models.Model):
    item_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null= True, blank=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=9)
    unit_expenses_on_work = models.DecimalField(decimal_places=2, max_digits=9)
    date_made = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.item_name + " " + str(self.quantity)

class FurniturePurchase (models.Model):
    total_purchase = models.DecimalField(decimal_places=2, max_digits=9, default=0.0)
    date_sold = models.DateTimeField(auto_now_add= True)

    """ def save(self, *args, **kwargs) -> None:
        if self.furnitureInventory.quantity > self.quantity:
            self.furnitureInventory.quantity = self.furnitureInventory.quantity - self.quantity
            self.total_price = self.quantity * self.furnitureInventory.unit_price
        super(FurniturePurchase, self).save(*args, **kwargs)
 """
class FurnitureItemPurchase (models.Model):
    furniture = models.ForeignKey(FurnitureInventory,  related_name="furniture", on_delete=CASCADE)
    purchase = models.ForeignKey(FurniturePurchase, related_name="purchase" , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def save(self, *args, **kwargs):
        self.furniture.quantity = int(self.furniture.quantity) - int(self.quantity)
        self.furniture.save()
        super(FurnitureItemPurchase, self).save(*args, **kwargs)

class FurnitureSupply(models.Model):
    furniture = models.ForeignKey(FurnitureInventory,  related_name="furnituresupply", on_delete=CASCADE)
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.furniture.quantity = self.furniture.quantity + self.quantity
        self.furniture.save()
        super(FurnitureSupply, self).save(*args, **kwargs)