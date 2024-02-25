from django.contrib import admin

# Register your models here.
from .models import Product,Blog

class SerAdmin(admin.ModelAdmin):
    li_dis=('image','name','price','description')

class BlogAdd(admin.ModelAdmin):
    li_blog=('date','author','title','content','image')

admin.site.register(Product,SerAdmin)
admin.site.register(Blog,BlogAdd)