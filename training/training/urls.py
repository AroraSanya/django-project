"""training URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
# from django.confimport setting
from blog.views import update_blog,delete_blog,login_user,home,logout_user,registered_user,publish_blog,update_user,publish_blog,CreateFormview, list_all_blogs, Blogview
from product.views import create_product,list_all_products,delete_product,add_to_cart,del_cart, cart_list,login,register_user,home_product,Contact_Us,logout_user_pro,add_wishlist,order_create, checkout, address_create, increment_item, decrement_item

urlpatterns = [
    path('',home_product,name='product_home'),
    path('admin/', admin.site.urls),
    path('create/blog',CreateFormview.as_view(),name='create-blog'),
    path('del/blog',Blogview.as_view(),name='blog'),


    path('',home,name='home page'),
    # path('hi/',csrf_exempt(hello)),
    # path('form/',form_view),
    # path('demo/create',create_blog,name='creating'),
    path('demo/list',list_all_blogs,name='listing'),
    path('demo/<int:id>/update',update_blog,name='updating'),
    path('demo/<int:id>/delete',delete_blog,name='deleting'),
    path('login/blog',login_user,name='bloglogin'),  
    path('change_pass/',update_user,name='pasword_update'),
    path('logout/',logout_user,name='logout'),
    path('registered/',registered_user,name='registered'),
    # path('publish/',publish_blog,name='published')
    path('publish/blog_publish/<int:id>',publish_blog,name='publish-blog'),

    ###################################
    
    path('productcreate',create_product,name='create'),
    path('logoutt',logout_user_pro,name='logout'),
    path('product/list',list_all_products,name='product-list'),
    path('product/delete',delete_product),
    path('add_to_cart/<int:id>',add_to_cart,name='add_cart'),
    # path('cart/<int:id>',del_cart),
    # path('register/user',registered_user),
    path('cart/list', cart_list,name='cart-list'),
    path('cart/del/<int:id>',del_cart, name='delete-cart'),
   

    path('register/', register_user,name='register'),
    path('login_product/',login,name='login'),
    path('contact/',Contact_Us,name='contactus'),
    path('wishlist-product/',add_wishlist,name='wishlist'),
    path('order/product',order_create,name='order'),
    path('checkout', checkout , name='checkout'),
    path('/increment/<int:id>',  increment_item, name='increment'),
     path('/decrement/<int:id>',  decrement_item, name='decrement'),
    
    path('address/create/',address_create ,name='address-create'),

    


    
   
]
    
