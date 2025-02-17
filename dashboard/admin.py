from django.contrib import admin
from .models import Products, Order
from django.contrib.auth.models import Group

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category',]

# Register your models here.

admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
#admin.site.unregister(Group)