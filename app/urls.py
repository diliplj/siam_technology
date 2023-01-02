from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('list/', views.ProductList.as_view({'get': 'get_queryset'}), name="product_list"),
    path('list/', views.ProductList.as_view(), name="product_list"),
]