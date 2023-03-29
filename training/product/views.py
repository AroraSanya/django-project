from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import ProductForm,RegisterForms,login_product,order_form,AddressForm,Order_items
from .models import Product,Cart,Order, AddressModel,Wishlist,Order_items
from product.cart_helper import login
from django.contrib.auth import authenticate,login as auth,logout
from django.contrib import messages
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer
from rest_framework import status




class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class AddressModelSerializer(ModelSerializer):
    class Meta:
        model=AddressModel
        fields='__all__'


@api_view()
def list_product(request):
    products=Product.objects.all()
    return Response({"product":ProductSerializer(products,many=True).data})


@api_view(http_method_names=('post',))
def Create_Produt(request):
    Serializer=ProductSerializer(data=request.data)
    Serializer.is_valid(raise_exception=True)
    Serializer.save()
    return Response({"message":Serializer.data})

@api_view(http_method_names=('put',))
def Update_Produt(request,pk):
    product=Product.objects.get(id=pk)
    Serializer=ProductSerializer(product,data=request.data)
    Serializer.is_valid(raise_exception=True)
    Serializer.save()
    return Response({"message":Serializer.data})
    

@api_view(http_method_names=('delete',))
def Delete_Produt(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return Response({"message":"successfully deleted"})


@api_view(http_method_names=('patch',))
def Partial_Update_Produt(request,pk):
    product=Product.objects.get(id=pk)
    Serializer=ProductSerializer(product,data=request.data,partial=True)
    Serializer.is_valid(raise_exception=True)
    Serializer.save()
    return Response({"message":Serializer.data})
    

@api_view(http_method_names=('post',))
def create_address(request):
    serializer=AddressModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'Address':serializer.data},status=status.HTTP_201_CREATED)
 

@api_view()
def address_list(request):
    addresses = AddressModel.objects.all()
    return Response({'Address':AddressModelSerializer(addresses,many=True).data},status=status.HTTP_200_OK)



@api_view(http_method_names=('put',))
def update_address(request, pk):
    address = AddressModel.objects.get(id=pk)
    serializer = AddressModelSerializer(address, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'Address':serializer.data}, status=status.HTTP_200_OK)




@api_view(http_method_names=('delete',))
def delete_address(request, pk):
    address = AddressModel.objects.get(id=pk)
    address.delete()
    
    return Response({'message':"Successfully Deleted"}, status=status.HTTP_202_ACCEPTED)


























#M-V-T######################################################################################
# from .models import MyModel

# def upload_picture(request):
#     if request.method == 'POST':
#         picture = request.FILES['picture']
#         MyModel.objects.create(picture=picture)
#         return render(request, 'success.html')
#     return render(request, 'profile_product.html')


def home_product(request):
    return render(request,'product_home.html')

# def profile(request):
#     form=profileForms()
#     return render(request,'profile_product.html',{'form':form})



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
        form_Product = ProductForm(request.POST,request.FILES)
        if form_Product.is_valid():
            form_Product.save()
            return redirect('product_home')
    return render(request,'create.html', {'form': form_Product})
    
def list_all_products(request):
    product = Product.objects.all()
    paginator = Paginator(product, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'list_all_product.html', {'page_obj': page_obj})   

def product_details(request, **kwargs):
      if id:=kwargs.get('id'):
            product = Product.objects.get(id=id)
            category= Product.objects.filter(category = product.category)
      return render(request,'product_details.html',{'product':product,'category':category})


def delete_product(request,**kwargs):
    if id:=kwargs.get('id'):
        product = Product.objects.get(id=id)
        product.delete()
    product = product.objects.all()
    return render(request,'list_all.html', {'product': product})


def add_to_cart(request,**kwargs):
     if id:=kwargs.get('id'):
            product = Product.objects.get(id=id)
            Cart.objects.create(product1_id=product.pk,quantity=1, user_id_id= request.user.id)
     return redirect('cart-list')

def increment_item(request, **kwargs):
    if id:=kwargs.get('id'):
        cart  = Cart.objects.get(id=id)
      
        cart.quantity= int(cart.quantity)+ 1
        print(cart.quantity)
        cart.save()
        return redirect('cart-list')
    return render(request, 'cart_list.html')

def decrement_item(request, **kwargs):
    if id:=kwargs.get('id'):
        cart  = Cart.objects.get(id=id)
      
        cart.quantity= int(cart.quantity)- 1
        print(cart.quantity)
        cart.save()
        return redirect('cart-list')
    return render(request, 'cart_list.html')   

def del_cart(request,**kwargs):
    if id:=kwargs.get('id'):
            cart= Cart.objects.get(id=id)
            cart.delete()
    return redirect('cart-list')

def cart_list(request):
    cart = Cart.objects.all()
    print(cart)
    # for p in cart:
    #     print(p.product1.price)
    # total_price  = sum(p.product1.price  for p in cart )
    return render(request,'cart_list.html', {'Cart': cart}) 

def Contact_Us(request):
    return render(request,'contact.html')

def add_wishlist(request,**kwargs):
    if pk := kwargs.get('id'):
        product = Product.objects.get(id = pk)
        # wishlist = request.session.get('wishlist',[])
        Wishlist.objects.create(user_id=request.user.id,product_id = product.pk)
        # item = {'name_of_product':product.name, 'Price':product.price, 'Id':product.pk}
        # wishlist.append(item)
        # request.session['wishlist'] = wishlist
    return redirect('get-wishlist')

def get_wishlist(request):
    wishlist  = Wishlist.objects.filter(user_id = request.user.id)
    return render(request, 'wishlist.html', {'wishlist':wishlist})


def del_to_wishlist(request,**kwargs):
     if pk:= kwargs.get('id'):
         wishlist = Wishlist.objects.get(id=pk)
         wishlist.delete()
         return redirect('product_home')
     return render(request,'wishlist.html', {'wishlist':wishlist})


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
            messages.success(request,'Login Successfully')
        return redirect('home page')
    else:
        print("please enter valid details for login ")
    return render(request,'login.html',{'form':form})

def logout_user_pro(request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return render(request,'product_home.html')

def address_create(request):
    form= AddressForm()
    if request.method == 'POST':
        form= AddressForm(request.POST)
        if form.is_valid():
            print("yesssss")
            instance = form.save(commit=False)
            instance.user_id_id = request.user.id
            form.save()
        return redirect('product_home') 
    return render(request,'address.html',{'form': form})


def order_create(request):
    cart = Cart.objects.filter(user_id_id=request.user.id)
    address = AddressModel.objects.get(user_id_id=request.user.id)
    for p in cart:
        total_cost = int(p.quantity) * p.product1.price
        Order.objects.create(user_id_id=request.user.id, product_id=p.product1.pk,address_id=address.pk, total_cost=total_cost)
    messages.success(request,'Ordered Successfully')
    return redirect('product_home')

def order_item(request,o_id,**kwargs):
    cart=request.objects.all()
    if id:=kwargs.get('id'):
        product=Product.objects.get(id=id)
#         # print(product.id)
        cart = Cart.objects.create(product1_id=product.id)
        cart.save()
    cart=Cart.objects.all()
    for p in cart:
        total=int(p['price'])*p['quantity']
        Order_items.objects.create(order_id=o_id, product_id=p['id'],price_items=total)
        print("yessssssssssssssssssssssssssssssssss")

def checkout(request):
    cart = Cart.objects.filter(user_id_id=request.user.id)
    address = AddressModel.objects.get(user_id_id=request.user.id)

    total_cost = sum(int(p.quantity) * p.product1.price for p in cart)
    print(total_cost)
    return render(request, 'checkout.html', {'cart':cart,'total':total_cost, 'address':address})

def profile_user(request):
    return render(request,'profile_product.html')

def change_password(request):
    print(request.method)
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            # /main_pass = request.POST.get('confirm_password')
            user = User.objects.get(username = username)
            print(user)
            user.set_password(password)
            user.save()
            return redirect('login')
    return render(request,'change_pass.html')


    

# def add_to_cart(request,**kwargs):
#     if id:=kwargs.get('id'):
#         product=Product.objects.get(id=id)
#         # print(product.id)
#         cart = Cart.objects.create(product1_id=product.id)
#         cart.save()
#     cart=Cart.objects.all()
#     return render(request,'add_to_cart.html',{'cart':cart})
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

# def delete_cart(request,**kwargs):
#     if id:=kwargs.get('id'):
#         cart = Cart.objects.get(id=id)
#         cart.delete()
#     cart = Cart.objects.all()
#     return render(request,'list_all_product.html', {'cart': cart})



# def registered_user(request):
#     user_login=request.session['user_login']   
#     return render(request)  


# def register(request):
#     return render(request,'register.html')

