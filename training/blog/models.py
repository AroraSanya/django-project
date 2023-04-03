from django.db import models


# Create your models here.
class Blog(models.Model):
    title =models.CharField(max_length=20)
    published_on=models.DateTimeField()
    author=models.CharField(max_length=44)
    description=models.TextField()
    is_published= models.BooleanField(default=False)

    class Meta:
        permissions=[('can_publish','Can Publish blog')]
        

class User(models.Model):
    f_name=models.CharField(max_length=44)
    l_name=models.CharField(max_length=44)
    bio = models.CharField(max_length=1000,null=True)
    number= models.CharField(max_length=32,null=True)
    city= models.CharField(max_length=50,null=True)
    zip= models.CharField(max_length=30,null=True)


