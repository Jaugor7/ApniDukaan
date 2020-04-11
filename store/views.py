from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Shop, Item
import random

# Create your views here.
def Index(request):

    if request.method == 'POST':
        if 'consumer' in request.POST:
            print('Consumer Found')
            return HttpResponseRedirect('consumer')

        elif 'new_retailer' in request.POST:
            print('New Retailer Found')
            return HttpResponseRedirect('new_retailer')  #redirect takes page url as argument

        elif 'shop_id' in request.POST:
            shop_id = request.POST['shop_id']
            print("Existing Retailer Found.. entering shop with specific id: ", shop_id)
            return FindShop(request, int(shop_id))

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

def addItem(request):
    added_date = timezone.now()
    item_name = request.POST['item_name']
    item_price = request.POST['item_price']
    item_unit = request.POST['item_unit']
    # retailer_key = 
    Item.objects.create(name = item_name, price = item_price, unit=item_unit)
    return HttpResponseRedirect('/')

# def Retailer(request):
    
#     if request.POST.get('shop_id'):
#         # get_shopDetailsFrom Database
#         # if show exists:
#         return HttpResponseRedirect('retailer/showshop')

    return render(request, 'store/retailer.html') #render takes html page as argument

def valid(shop_id):
    all_id = [int(t.shop_key) for t in Shop.objects.all()]
    if shop_id in all_id:
        return True
    return False


def FindShop(request, shop_id):
    if valid(shop_id):
        return render(request, 'store/showshop.html')
    return render(request, "store/notFound.html")
        


