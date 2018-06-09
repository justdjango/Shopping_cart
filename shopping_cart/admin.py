from django.contrib import admin

from .models import OrderItem, Order, Transaction

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Transaction)
