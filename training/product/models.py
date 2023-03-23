from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name =models.CharField(max_length=50)
    price=models.IntegerField()
    quality = models.TextField()

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