

from django.urls import path
from . import views


urlpatterns = [
    path ("", views.home, name="home"),
    path("products/", views.Products, name="Products"),
    path("product_list/", views.product_list, name="product_list"),
]
