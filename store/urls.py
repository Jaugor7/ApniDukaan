from django.urls import path
from . import views

urlpatterns= [
    path('', views.Index, name='index'),
    path('new_retailer', views.addRetailer, name='add_retailer'),
    path('consumer', views.Consumer, name='consumer'),
    # path('showshop', views.ShowShop, name= 'shop'),

]