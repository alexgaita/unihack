from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from .models import *
import json
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order ={'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

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
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order ={'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products':products,'cartItems':cartItems}
    return render(request,'cantina/product_list.html',context)



def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order ={'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context={'items':items , 'order':order , 'cartItems':cartItems}
    return render(request,'cantina/cart.html',context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order ={'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

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
