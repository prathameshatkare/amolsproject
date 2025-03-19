from django.shortcuts import render
from .forms import Product_form
# Create your views here.
from .models import Product

def home(request):
    return render (request,'electronics/home.html')





def product_detail(request):
    prod = Product.objects.all()
    form = Product_form()

    if request.method=='POST':
        form =Product_form(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'electronics/product_detail.html',{"prod":prod, "form":form})
    

     

         