from django.db import models

# Create your models here.
class Product(models.Model):
    name =models.CharField(max_length=50)
    price=models.IntegerField()
    quality=models.TextField()

class Cart(models.Model):
  product1 = models.ForeignKey("product", on_delete=models.CASCADE)
  # active = models.BooleanField(default=True)
  # order_date = models.DateField(null=True)
  # payment_type = models.CharField(max_length=100, null=True)
  # payment_id = models.CharField(max_length=100, null=True)