from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from products.models import Product

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ebooks = models.ManyToManyField(Product, blank=True)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

    user_profile, created = Profile.objects.get_or_create(user=instance)

    if user_profile.stripe_id is None or user_profile.stripe_id == '':
        new_stripe_id = stripe.Customer.create(email=instance.email)
        user_profile.stripe_id = new_stripe_id['id']
        user_profile.save()


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)

# freire1996@gmail.com
# matt1234

'''

<Customer customer id=cus_CzugkhqEYJXyuF at 0x00000a> JSON: {
  "id": "cus_CzugkhqEYJXyuF",
  "object": "customer",
  "account_balance": 0,
  "created": 1528265466,
  "currency": "usd",
  "default_source": null,
  "delinquent": false,
  "description": null,
  "discount": null,
  "email": null,
  "invoice_prefix": "B35D489",
  "livemode": false,
  "metadata": {
  },
  "shipping": null,
  "sources": {
    "object": "list",
    "data": [

    ],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/customers/cus_CzugkhqEYJXyuF/sources"
  },
  "subscriptions": {
    "object": "list",
    "data": [

    ],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/customers/cus_CzugkhqEYJXyuF/subscriptions"
  }
}

'''




