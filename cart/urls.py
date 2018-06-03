from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profiles/', include('accounts.urls', namespace='accounts')),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^cart/', include('shopping_cart.urls', namespace='shopping_cart'))
]
