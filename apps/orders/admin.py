from django.contrib import admin

# Register your models here.
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    
admin.site.register(Order, OrderAdmin)
