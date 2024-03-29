from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    tagname = models.CharField(max_length=70)
    def __str__(self):
        return self.tagname

class Product(models.Model):
    name =models.CharField(max_length=50,blank = True)
    price=models.IntegerField(blank= True)
    quality = models.TextField(blank =True)
    image  = models.ImageField(upload_to='images/',null=True)
    category=models.CharField(max_length=50,null=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Cart(models.Model):
  product1 = models.ForeignKey(Product, on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  quantity=models.CharField(max_length=50)

class AddressModel(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Full name", max_length=1024)
    address1 = models.CharField("Address line 1", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024, blank=True, null=True)
    zip_code = models.CharField("ZIP", max_length=12)
    city = models.CharField("City", max_length=1024)
class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(User,related_name='address', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  related_name='product', on_delete=models.CASCADE)
    total_cost = models.FloatField(default=1)
    date = models.DateTimeField(auto_now=True)

class Wishlist(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)    

class Order_items(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price_items=models.CharField(max_length=200)

