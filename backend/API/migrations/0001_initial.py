# Generated by Django 4.2.6 on 2023-10-06 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Product Name')),
                ('price', models.CharField(max_length=200, verbose_name='Price')),
                ('quantity', models.CharField(max_length=200, verbose_name='Available Quantity')),
                ('sold', models.CharField(max_length=100, verbose_name='Sold Quantity')),
                ('desc', models.TextField(verbose_name='Product Description')),
                ('orders', models.CharField(default='0', max_length=50, verbose_name='Orders for Product')),
                ('added_on', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Product Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('business_title', models.CharField(max_length=50, verbose_name='Business Title')),
                ('business_type', models.CharField(max_length=50, null=True, verbose_name='Business Type')),
                ('business_desc', models.TextField(null=True, verbose_name='Business Description')),
                ('seller_desc', models.TextField(verbose_name='Seller Description')),
                ('img', models.ImageField(default='', upload_to='seller-profiles', verbose_name='Seller Profile Img')),
                ('is_allowed', models.BooleanField(default=False, verbose_name='Allow To Sell')),
                ('is_active', models.BooleanField(default=True, verbose_name='Seller is Active')),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='product-images', verbose_name='Product img')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.product_categorie'),
        ),
    ]
