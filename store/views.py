from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def Index(request):

    if request.method == 'POST':
        if 'consumer' in request.POST:
            print('Consumer Found')
            return HttpResponseRedirect('consumer')

        elif 'retailer' in request.POST:
            print('retailer found')
            return HttpResponseRedirect('retailer')

    return render(request, 'index.html')

def Consumer(request):
    return render(request, 'store/consumer.html')

def Retailer(request):
    
    if request.POST.get('shop_id'):
        # get_shopDetailsFrom Database
        # if show exists:
        return HttpResponseRedirect('retailer/showshop')

    return render(request, 'store/retailer.html')

def ShowShop(request):

    return render(request, 'store/showshop.html')


