from django.shortcuts import render

# Create your views here.
from .models import Product

def home(request):
    return render (request,'electronics/home.html')


def product_detail(request):

    prod = Product.objects.all()
    return render(request, 'electronics/product_detail.html',{"prod":prod})