from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Product_Categorie(models.Model):
    
    category_name = models.CharField(max_length=50, verbose_name="Product Category Name")
    

    def __str__(self):

        return self.category_name


class Product(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, verbose_name='Product Name')
    category = models.CharField(max_length=100, verbose_name='Product Category')
    price = models.CharField(max_length=200, verbose_name='Price')
    quantity = models.CharField(max_length=200, verbose_name='Available Quantity')
    sold = models.CharField(max_length=100, verbose_name='Sold Quantity')

    desc = models.TextField(verbose_name='Product Description')
    orders = models.CharField(max_length=50, default='0', verbose_name='Orders for Product')
    added_on = models.DateTimeField(auto_now_add=True, verbose_name="Added On")


    def __str__(self):

        return self.name     



class Product_Image(models.Model):

    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='product-images', null=False, verbose_name='Product img')

    def __str__(self):

        return self.product.name 




class SellerProfile(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    seller_desc = models.TextField(verbose_name='Seller Description')
    
    business_title = models.CharField(max_length=50, verbose_name='Business Title')
    business_type = models.CharField(max_length=50, null=True, verbose_name='Business Type')
    business_desc = models.TextField(null=True, verbose_name='Business Description')


    img = models.ImageField(upload_to='seller-profiles', default='', verbose_name='Seller Profile Img')

    is_allowed = models.BooleanField(default=False, verbose_name='Allow To Sell')
    is_active = models.BooleanField(default=True, verbose_name='Seller is Active')
    
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.user.username 

