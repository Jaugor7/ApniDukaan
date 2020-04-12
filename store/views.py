from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Shop, Item
import random
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def Index(request):

    if request.method == 'POST':
        if 'consumer' in request.POST:
            print('Consumer Found')
            return HttpResponseRedirect('consumer')

        elif 'new_retailer' in request.POST:
            print('New Retailer Found')
            return HttpResponseRedirect('new_retailer')  #redirect takes page url as argument

    return render(request, 'index.html')

def randomKeyGenerator():

    presentKeys = [int(t.shop_key) for t in Shop.objects.all()]
    while(True):
        generated_key = int(random.random()*10000)
        if generated_key not in presentKeys:
            return generated_key

def addRetailer(request):
    return render(request, 'store/add_retailer.html')

def Consumer(request):
    return render(request, 'store/consumer.html')

def valid(shop_id):
    all_id = [t.shop_key for t in Shop.objects.all()]
    if shop_id in all_id:
        return True
    return False

def addItem(request, shop_id, item_name, item_price, item_unit):
    print(shop_id ,item_name,item_price, item_unit)
    shop = Shop.objects.get(shop_key = shop_id)
    Item.objects.create(name = item_name, price = item_price, unit=item_unit, item_key = shop)
    print("Item Added Successfully")
    return HttpResponseRedirect('/')

def deleteItem(request, shop_id, item_id):
    Item.objects.get(pk = item_id).delete()
    print('Item from shop' +str(shop_id)+'Deleted successfully with item id as', item_id) 
    return HttpResponseRedirect('/')

def EnterShop(request):
    if request.method == "GET":
        shop_id = int(request.GET['shop_id'])

    if request.method == "POST":
        if 'add' in request.POST:
            shop_id = int(request.POST['shop_id'])
            item_name = request.POST['item_name']
            item_price = request.POST['item_price']
            item_unit = request.POST['item_unit']
            addItem(request, shop_id, item_name, item_price, item_unit)

        elif 'delete' in request.POST:
            item_id = int(request.POST['delete'])
            deleteItem(request, shop_id, item_id)

    if valid(shop_id):
        shop_item = Item.objects.filter(item_key = shop_id)
        send_to_front = {
            'item_list': shop_item,
            'shop_id': shop_id,
            }
        return render(request, "store/EnterShop.html", send_to_front)
   
    return render(request, "store/notFound.html")