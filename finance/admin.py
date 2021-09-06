from django.contrib import admin
from .models import MachineWork, Operator, Staff

# Register your models here.
admin.site.register(MachineWork)
admin.site.register(Operator)
admin.site.register(Staff)