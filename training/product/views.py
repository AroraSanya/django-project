from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import ProductForm,RegisterForms,login_product
from .models import Product,Cart
from product.cart_helper import add_cart,delete_cart,login
from django.contrib.auth import authenticate,login as auth,logout
from django.contrib import messages

# Create your views here.

def home_product(request):
    return render(request,'product_home.html')


def register_user(request):
    form=RegisterForms()
    if request.method=='POST':
        username = request.POST.get('username', None)
        userpass = request.POST.get('password', None)
        user = User.objects.create_user(username=username,password=userpass)
        user.save()
        print(request.user)
        messages.success(request,'Register Successfully')
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


def add_to_cart(request,**kwargs):
    helper_cart=add_cart(request,**kwargs)
    return redirect('cart/list')

def del_cart(request,**kwargs):
    cart=delete_cart(request,**kwargs)
    print(cart)
    return redirect('/cart/list')

def cart_list(request):
    cart= request.session['cart']
    print(cart)
    return render(request,'add_to_cart.html', {'cart':cart})

def Contact_Us(request):
    return render(request,'contact.html')

# def registered_user(request):
#     user_login=request.session['user_login']   
#     return render(request)  


# def register(request):
#     return render(request,'register.html')

def login(request):
    form = login_product()
    if request.method == "POST":
        print(request.user)
        name= request.POST['username']
        password = request.POST.get('password')
        user = authenticate(request,username=name,password=password)
        if user is not None:
            print("yes")
            auth(request,user)
            print(request.user)
            return redirect('home page')
        else:
            print("please enter valid details for login ")
    return render(request,'login.html',{'form':form})

def logout_user_pro(request):
    logout(request)
    return render(request,'product_home.html')

def add_to_cart(request,**kwargs):
    if id:=kwargs.get('id'):
        product=Product.objects.get(id=id)
        # print(product.id)
        cart = Cart.objects.create(product1_id=product.id)
        cart.save()
    cart=Cart.objects.all()
    return render(request,'add_to_cart.html',{'cart':cart})
# # WITH-----SESSION 
# def add_to_cart(request,**kwargs):
#     if id:=kwargs.get('id'):
#         product=Product.objects.get(id=id)
#         cart_session = request.session.get('cart', [])
#         cart_items = {'Name': product.name, 'price':product.price,'quality':product.quality}
#         cart_session.append(cart_items)
#         request.session['cart'] = cart_session
#         print(request.session['cart'])
#     return render(request,'add_to_cart.html')

def delete_cart(request,**kwargs):
    if id:=kwargs.get('id'):
        cart = Cart.objects.get(id=id)
        cart.delete()
    cart = Cart.objects.all()
    return render(request,'list_all_product.html', {'cart': cart})



