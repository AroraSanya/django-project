from django.shortcuts import render
from .forms import ProductForm

# Create your views here.
def create_product(request): 
    form_blog = ProductForm()
    if request.method == 'POST':
        form_Product = ProductForm(request.POST)
        if form_Product.is_valid():
            form_Product.save()
    return render(request,'create.html', {'form': form_Product})
    
def list_all_products(request):
    product = product.objects.all()
    return render(request,'list_all_product.html', {'product': product})    

def delete_product(request,**kwargs):
    if id:=kwargs.get('id'):
        product = product.objects.get(id=id)
        product.delete()
    product = product.objects.all()
    return render(request,'list_all.html', {'product': product})

def add_to_cart():
