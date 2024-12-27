from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Customer(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES ={
    ('BC','bambooCraft'),
    ('MC','metalCraft'),
    ('JC','juteCraft'),
    ('PC','paintingCraft'),
}
class Product(models.Model):
    title =models.CharField(max_length=100)
    price =models.FloatField()
    dis_price =models.FloatField()
    description =models.TextField()
    category =models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image =models.ImageField(upload_to='productimage')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    
    def __str__(self):
        return str(self.id)


STATUS_CHOICES ={
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
}

class OrderPlaced(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date =models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

    
class Shop(models.Model):
    
    username=models.CharField(max_length=200)
    shopname=models.CharField(max_length=200)
    craftname=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=50)
      
      
    def __str__(self):
        return str(self.id)


       
class Profile(models.Model):
    
    username=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    email=models.EmailField( max_length=254)
    address=models.CharField(max_length=300)
    mobile_no=models.CharField(max_length=50)
      
      
    def __str__(self):
        return str(self.id)



       
class Contactus(models.Model):
    
    username=models.CharField(max_length=200)
    email=models.EmailField( max_length=254)
    address=models.CharField(max_length=300)
    
      
      
    def __str__(self):
        return str(self.id)          
   