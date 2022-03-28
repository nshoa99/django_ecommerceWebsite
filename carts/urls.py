from django.urls import path

from nshop import views
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('decrease_quantity/<int:product_id>/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity' ),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item')
]
