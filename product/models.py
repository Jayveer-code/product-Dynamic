from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='news/',max_length=300,null=True,default=None)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()


class Blog(models.Model):
    date = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/blog_images', null=True, blank=True)