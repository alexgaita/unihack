from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import *
# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cantina/index.html')

class About(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'cantina/about.html')


class Register(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'cantina/register.html')
class Meniu(ListView):
    context_object_name = 'products'
    model = Product


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order ={'get_cart_total': 0, 'get_cart_items': 0}

    context={'items':items , 'order':order}
    return render(request,'cantina/cart.html',context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order ={'get_cart_total': 0, 'get_cart_items': 0}

    context={'items':items , 'order':order}
    return render(request,'cantina/checkout.html',context)
