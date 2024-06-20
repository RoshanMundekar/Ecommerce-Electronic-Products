

import datetime
from random import choice
from django.utils import timezone
from django.db import models
from ckeditor .fields import RichTextField
from django.contrib.auth.models import User


class Categories(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Brand(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Color(models.Model):  
    name=models.CharField(max_length=255)
    code=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Filter_Price(models.Model):
    FILTER_PRICE=(
        ('10000 To 20000 ','10000 To 20000 '),
        ('200000 To 30000 ','20000 To 30000 '),
        ('30000 To 40000 ','30000 To 40000 '),
        ('40000 To 50000 ','40000 To 50000 ')

    )  
    price=models.CharField(choice==FILTER_PRICE,max_length=60)  
    def __str__(self):
        return self.price



class Product(models.Model):
    CONDITION=(('New','New'),('Old','Old'))
    STOCK=(('IN STOCKS','IN STOCKS'),('OUT OF STOCKS','OUT OF STOCKS'))
    STATUS=(('Publish','Publish'),('Drafts','Drafts'))
    Uniqe_id = models.CharField(unique=True,max_length=200,null=True ,blank=True)
    image = models.ImageField(upload_to='Product_images/img')  
    name = models.CharField(max_length=200)    
    price = models.IntegerField()    
    condition = models.CharField(choices= CONDITION ,max_length=100)    
    name = models.CharField(max_length=200)    
    Information = RichTextField(null=True)
    description = RichTextField(null=True) 
    stock = models.CharField(choices= STOCK ,max_length=200)    
    status = models.CharField(choices= STATUS ,max_length=200)  
    created_date=models.DateTimeField(default=timezone.now)
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)  
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE) 
    color = models.ForeignKey(Color,on_delete=models.CASCADE) 
    filter_price = models.ForeignKey(Filter_Price,on_delete=models.CASCADE) 
    def __str__(self):
        return self.name


def save(self,*args,**kwargs):
    if self.Uniqe_id is None and self.created_date and self.id:
        self.Uniqe_id = self.create_date.strtime('75%Y%m%D23') + str(self.id)
    return super.save(*args,**kwargs)   

def __str__(self):
        return self.name


class Images(models.Model):
    image=models.ImageField(upload_to='Product_images/img')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
   


class Tag(models.Model):
    name=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Contact_us(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=300)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
    
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    address=models.TextField()
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    postcode=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField(max_length=200)
    additional_info=models.TextField()
    amount=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=300,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True)
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class Orderitem (models.Model):
    Order=models.ForeignKey(Order,on_delete=models.CASCADE)
    prduct=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Product_images/Order_Img")
    quantity=models.CharField(max_length=20)
    price=models.CharField(max_length=50)
    total=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.Order.user.username
    
       
    
       
        