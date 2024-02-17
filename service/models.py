from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='news/',max_length=300,null=True,default=None)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

  