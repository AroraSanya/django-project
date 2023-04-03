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
from product.views import create_product,list_all_products,delete_product,add_to_cart,del_cart, cart_list,login,register_user,home_product,Contact_Us,logout_user_pro,order_create, checkout, address_create, increment_item, decrement_item,profile_user,change_password,add_wishlist,get_wishlist,del_to_wishlist,product_details,order_item,list_product,Create_Produt,Update_Produt,Delete_Produt,Partial_Update_Produt,create_address,address_list,update_address,delete_address,Partial_Update,product_get_view,login_user_token,logout_users
from django.conf.urls.static import static 
from django.conf import settings
from product.views import ProductListView,ProductDetailView,ProductCreateView,ProductUpdateView,ProductDeleteView
from blog.views import *


urlpatterns = [
    ################# blog-API #################
    path('createblog',CreateApiviews.as_view()),
    path('listblog',ListAPIviews.as_view()),
    path('retrieveblog/<int:pk>',RetrieveApiviews.as_view()),
    path('listcreateblog',ListCreateapiviews.as_view()),



    # path('',home,name='home page'),
    path('',home_product,name='product_home'),
    path('admin/', admin.site.urls),
    # path('create/blog',CreateFormview.as_view(),name='create-blog'),
    path('del/blog',Blogview.as_view(),name='blog'),
    path('user_fullname',ListUserCreateApi.as_view()),


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

    ############################################################################
    path('List/', list_product,name='list-API'), 
    path('Create/', Create_Produt,name='create-API'),
    path('Update/<int:pk>', Update_Produt,name='update-API'),
    path('Delete/<int:pk>', Delete_Produt,name='Delete-API'),
    path('Partial_Update/<int:pk>', Partial_Update_Produt,name='Partial_Update-API'),
    path('createaddress/',create_address,name='Partial_Update-API'),
    path('listaddress/',address_list,name='Partial_Update-API'),
    path('Updateaddress/<int:pk>', update_address,name='updateaddress-API'),
    path('Deleteaddress/<int:pk>', delete_address,name='Deleteaddress-API'),
    path('PartialUpdate/<int:pk>', Partial_Update,name='Partial-API'),
    path('productget/<int:pk>',product_get_view,name='product_get'),
    path('login_usertoken/',login_user_token,name='loginusertoken'),
    path('logout_usertoken/',logout_users,name='logoutusertoken'),
#######   Class-based-view   ################
    path('list_class/',ProductListView.as_view(),name='product-list'),
    path('details_class/<int:pk>',ProductDetailView.as_view(),name='productdetails'),
    path('create_class/',ProductCreateView.as_view(),name='create'),
    path('update_class/<int:pk>',ProductUpdateView.as_view()),
    path('delete_class/<int:pk>',ProductDeleteView.as_view()),








    #############################################################################
    # path('productcreate',create_product,name='create'),
    path('logoutt',logout_user_pro,name='logout'),
    # path('product/list',list_all_products,name='product-list'),
    path('product/delete',delete_product),
    path('add_to_cart/<int:id>',add_to_cart,name='add_cart'),
    # path('cart/<int:id>',del_cart),
    # path('register/user',registered_user),
    path('cart/list', cart_list,name='cart-list'),
    path('cart/del/<int:id>',del_cart, name='delete-cart'),
   
     path('List/', list_product,name='list-API'), 
    path('register/', register_user,name='register'),
    path('login_product/',login,name='login'),
    path('contact/',Contact_Us,name='contactus'),
    path('wishlist-product/<int:id>',add_wishlist,name='wishlist'),
    path('wishlist-get/',get_wishlist,name='get-wishlist'),
    path('wishlist-del/<int:id>',del_to_wishlist,name='del-wishlist'),

    path('order/product',order_create,name='order'),
    path('checkout', checkout , name='checkout'),
    path('increment/<int:id>',  increment_item, name='increment'),
    path('decrement/<int:id>',  decrement_item, name='decrement'),
    path('address/create/',address_create ,name='address-create'),
    path('profile/',profile_user ,name='profile_user'),
    path('change-pass/',change_password ,name='changepass'),
    # path('details/<int:id>',product_details ,name='productdetails'),
    path('items/>',order_item ,name='orderitem'),
    #  path('items/>',search ,name='orderitem'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
