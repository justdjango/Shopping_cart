from django.contrib import admin

from .models import OrderItem, Order #, PaymentMethod, Payment

admin.site.register(OrderItem)
admin.site.register(Order)
# admin.site.register(Payment)
# admin.site.register(PaymentMethod)