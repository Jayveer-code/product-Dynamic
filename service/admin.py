from django.contrib import admin

# Register your models here.
from .models import Product

class SerAdmin(admin.ModelAdmin):
    li_dis=('image','name','price','description')

admin.site.register(Product,SerAdmin)