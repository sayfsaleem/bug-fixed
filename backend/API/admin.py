from django.contrib import admin
from .models import * 


class Product_Admin(admin.ModelAdmin):


    list_display = ['title','category', 'price', 'quantity']
    search_fields = ['title', 'category', 'price', 'quantity']




admin.site.site_title = "Admin Site"

admin.site.register(Product, Product_Admin)