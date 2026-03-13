from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.get_orders),
    path('create-order/', views.create_order),
]