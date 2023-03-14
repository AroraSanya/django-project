from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import ProductForm,RegisterForms
from .models import Product,Cart


# Create your views here.
def registered_user(request):
    form=RegisterForms()
    if request.method=='POST':
        userName = request.POST.get('username', None)
        userPass = request.POST.get('password', None)
        user = User.objects.create_user(userName, userPass)
        user.save()
    return render(request,'register.html', {'form': form})

    
def create_product(request): 
    form_Product = ProductForm()
    if request.method == 'POST':
        form_Product = ProductForm(request.POST)
        if form_Product.is_valid():
            form_Product.save()
    return render(request,'create.html', {'form': form_Product})
    
def list_all_products(request):
    product = Product.objects.all()
    return render(request,'list_all_product.html', {'product': product})    

def delete_product(request,**kwargs):
    if id:=kwargs.get('id'):
        product = Product.objects.get(id=id)
        product.delete()
    product = product.objects.all()
    return render(request,'list_all.html', {'product': product})

# def add_to_cart(request,**kwargs):
#     if id:=kwargs.get('id'):
#         product=Product.objects.get(id=id)
#         # print(product.id)
#         cart = Cart.objects.create(product1_id=product.id)
#         cart.save()
#     cart=Cart.objects.all()
#     return render(request,'add_to_cart.html',{'cart':cart})
# WITH-----SESSION 
def add_to_cart(request,**kwargs):
    if id:=kwargs.get('id'):
        product=Product.objects.get(id=id)
        cart_session = request.session.get('cart', [])
        cart_items = {'Name': product.name, 'price':product.price,'quality':product.quality}
        cart_session.append(cart_items)
        request.session['cart'] = cart_session
        print(request.session['cart'])
    return render(request,'add_to_cart.html')

def delete_cart(request,**kwargs):
    if id:=kwargs.get('id'):
        cart = Cart.objects.get(id=id)
        cart.delete()
    cart = Cart.objects.all()
    return render(request,'add_to_cart.html', {'cart': cart})



