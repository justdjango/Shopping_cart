from django.conf.urls import url

from .views import product_list

app_name = 'products'

urlpatterns = [
    url(r'^', product_list, name='product-list')
]
