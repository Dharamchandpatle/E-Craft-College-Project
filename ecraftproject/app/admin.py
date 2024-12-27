from django.contrib import admin
from .models import  Customer,Product,Cart,OrderPlaced,Shop,Profile,Contactus

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display =['id','user','name','address','city']

@admin.register(Shop)
class ShopModelAdmin(admin.ModelAdmin):
    list_display =['id','username','shopname','craftname','address','city']


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display =['id','username','gender','email','address','mobile_no']



@admin.register(Contactus)
class ContactusModelAdmin(admin.ModelAdmin):
    list_display =['id','username','email','address']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id','title','price','dis_price','description','category','product_image']

    
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display =['id','user','product','quantity']

    
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display =['id','user','product','quantity','ordered_date','status']
