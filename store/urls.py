from django.urls import path
from . import views

app_name = 'store'

urlpatterns= [
    path('', views.Index, name='index'),
    path('new_retailer', views.addRetailer, name='add_retailer'),
    path('consumer', views.Consumer, name='consumer'),
    path('EnterShop', views.EnterShop, name= 'enters_shop'),
    path('delete/<int:item_id>', views.deleteItem, name='delete'),
]