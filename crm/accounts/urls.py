from django.urls import path
from . import views

urlpatterns = [
    path('', views.ElectroIndex, name='ElectroIndex'),
    path('ElectroShop/', views.ElectroShop, name='ElectroShop'),
    path('ElectroContact/', views.ElectroContact, name='ElectroContact'),
    path('ElectroCart/', views.ElectroCart, name='ElectroCart'),
    path('ElectroCheckout/', views.ElectroCheckout, name='ElectroCheckout'),
    path('ElectroShopDetail/<int:pk>', views.ElectroShopDetail, name='ElectroShopDetail'),
    path('ShopByCategory/<int:CatID>', views.ShopByCategory, name='ShopByCategory'),


    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout_view/', views.checkout_view, name='checkout_view'),

    # path('cart/increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    # path('cart/decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    
    path('billing_add/', views.billing_add, name='billing_add'),
    path('billing_list/', views.billing_list, name='billing_list'),
]