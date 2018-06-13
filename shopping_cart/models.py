from __future__ import unicode_literals

from django.db import models

from accounts.models import Profile
from products.models import Product


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)


class Transaction(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    token = models.CharField(max_length=120)
    order_id = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.order_id

    class Meta:
        ordering = ['-timestamp']







        