from django.urls import path
from . import views

urlpatterns= [
    path('', views.Index, name='index'),
    path('retailer', views.Retailer, name='retailer'),
    path('consumer', views.Consumer, name='consumer'),
    path('retailer/showshop', views.ShowShop, name= 'shop'),

]