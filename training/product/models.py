from django.db import models

# Create your models here.
class Product(models.Model):
    name =models.CharField(max_length=50)
    price=models.IntegerField()
    quality=models.TextField()

class Cart(models.Model):
  product1 = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity=models.CharField(max_length=50)

class AddressModel(models.Model):
    user_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField("Full name", max_length=1024)
    address1 = models.CharField("Address line 1", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024, blank=True, null=True)
    zip_code = models.CharField("ZIP", max_length=12)
    city = models.CharField("City", max_length=1024)
class Order(models.Model):
    order_id = models.CharField(max_length=100, default="")
    date = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length= 500)
    mobile_no = models.CharField(max_length = 12)
    product = models.ForeignKey(Product,  related_name='product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=1)
    total_cost = models.FloatField(default=1)