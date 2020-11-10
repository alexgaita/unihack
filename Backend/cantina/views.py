from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
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
class Meniu(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'cantina/meniu.html')
class Cart(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'cantina/cart.html')
class Checkout(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'cantina/checkout.html')
