from django.db import models

# Create your models here.
class Product(models.Model):
    name =models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    # image=models.ImageField(upload_to=)
    quality=models.TextField()

class cart(models.Model):
  product1 = models.ForeignKey("product", on_delete=models.CASCADE)

