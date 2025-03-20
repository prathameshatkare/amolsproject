from django.shortcuts import render,redirect,get_object_or_404
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
            form = Product_form()
    return render(request, 'electronics/product_detail.html',{"prod":prod, "form":form})
    
def update_product(request,id):
    prod = get_object_or_404(Product,id=id)
    # form = Product_form(instance=prod)
    if request.method=='POST':
        form = Product_form(request.POST,instance=prod)
        if form.is_valid():
            form.save()
            return redirect('product_detail')
    else:
        form = Product_form(instance=prod)
    return render(request,'electronics/update_product.html',{"form":form,"prod":prod})
def delete_product(request,id):
    prod = get_object_or_404(Product,id=id)
    prod.delete()
    return redirect('product_detail')

         