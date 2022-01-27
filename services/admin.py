from django.contrib import admin
from .models import  *

# Register your models here.
admin.site.register(MachineWork)
admin.site.register(Operator)
admin.site.register(Staff)

admin.site.register(GeneralExpence)
admin.site.register(Salary)

admin.site.register(WoodFromBush)
admin.site.register(WoodSale)
admin.site.register(WoodItemSale)

admin.site.register(FurnitureInventory)
admin.site.register(FurniturePurchase)
admin.site.register(FurnitureItemPurchase)
admin.site.register(FurnitureSupply)
