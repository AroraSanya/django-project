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
from blog.views import create_blog,list_all_blogs,update_blog,delete_blog
from product.views import create_product,list_all_products,delete_product,add_to_cart,delete_cart,registered_user
urlpatterns = [
    path('admin/', admin.site.urls),
   
    # path('hi/',csrf_exempt(hello)),
    # path('form/',form_view),
    path('demo/create',create_blog),
    path('demo/list',list_all_blogs),
    path('demo/<int:id>/update',update_blog),
    path('demo/<int:id>/delete',delete_blog),
    path('productcreate',create_product),
    path('product/list',list_all_products),
    path('product/delete',delete_product),
    path('add_to_cart/<int:id>/add',add_to_cart),
    path('product/<int:id>/delete',delete_cart),
    path('register/user',registered_user),
    
   
]
    
