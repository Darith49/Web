from django.db import models
from .models import *
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):
    CategoryName = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.CategoryName}'

class Product(models.Model):
    categoryID = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    productName = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="img/products/", null=True, blank=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.CharField(max_length=200, null=True)
    shipping = models.CharField(max_length=200, null=True)
    rating = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f'{self.id} - {self.productName} | {self.categoryID.CategoryName}'

class ProductDetail(models.Model):
    productDescript = models.CharField(max_length=200, null=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    Description =  RichTextUploadingField(null=True)
    Information = RichTextUploadingField(null=True)
    Reviews = RichTextUploadingField(null=True)
    productDetailDate = models.DateTimeField (auto_now_add=True, null=True)
    def __str__(self):
        return f'{self.id} - {self.productID.productName}'
    

class CarouselSlide(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="img/carousel/")

    def __str__(self):
        return f'{self.id} - {self.title}'



class BannerOffer(models.Model):
    offer_text = models.CharField(max_length=200) 
    label = models.CharField(max_length=100)     
    product_name = models.CharField(max_length=200)
    old_price = models.FloatField()
    new_price = models.FloatField()
    image = models.ImageField(upload_to="img/banner/")

    def __str__(self):
        return f'{self.product_name}'



class PromoBox(models.Model):
    title = models.CharField(max_length=100)             
    description = models.CharField(max_length=200, blank=True) 
    discount_text = models.CharField(max_length=50)      
    image = models.ImageField(upload_to="img/promobox/")
    
    def __str__(self):
        return f'{self.id} - {self.title}'



class Banner(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="img/banners/", null=True, blank=True)

    # To know which banner is which (left or right)
    position = models.CharField(
        max_length=10,
        choices=[
            ('left', 'Left Banner'),
            ('right', 'Right Banner'),
        ],
        default='left'
    )

    def __str__(self):
        return f"{self.position} - {self.title}"



class BillingDetail(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    town = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    qr_code_image = models.ImageField(upload_to='qrcodes/', null=True, blank=True)
    total = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
