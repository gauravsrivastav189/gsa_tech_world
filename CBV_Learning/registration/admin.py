from django.contrib import admin

# Register your models here.
from .models import User, Delivery, Revenue


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'status')
    list_filter = ('status',)

@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount')
    list_filter = ('date',)

