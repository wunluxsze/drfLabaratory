from django.contrib import admin
from .models import Products, Order, Shift, Employee, Group
# Register your models here.
admin.site.register(Products)
admin.site.register(Shift)
admin.site.register(Order)
admin.site.register(Employee)
admin.site.register(Group)