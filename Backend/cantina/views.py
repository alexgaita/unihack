from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from .models import *
import datetime
import json
from .utils import cookieCart,cartData,guestOrder
# Create your views here.
def index(request):
    data= cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products':products,'cartItems':cartItems}
    return render(request,'cantina/index.html',context)

class About(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'cantina/about.html')


class Register(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'cantina/register.html')

def meniu(request):
    data= cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products':products,'cartItems':cartItems}
    return render(request,'cantina/product_list.html',context)



def cart(request):
    data= cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context={'items':items , 'order':order , 'cartItems':cartItems}
    return render(request,'cantina/cart.html',context)


def checkout(request):
    data= cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context={'items':items , 'order':order,'cartItems':cartItems}
    return render(request,'cantina/checkout.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('ProductId:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total==order.get_cart_total:
            order.complete = True
        order.save()


    else:
        customer , order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total==order.get_cart_total:
        order.complete = True
    order.save()
    return JsonResponse('Payment complete!', safe=False)
