
from django.views import View
from .models import  Customer,Product,Cart,OrderPlaced,Shop,Profile,Contactus
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from django.core.mail import send_mail

class ProductView(View):
 def get(self, request):
  bambooCraft =Product.objects.filter(category='BC')
  metalCraft =Product.objects.filter(category='MC')
  juteCraft =Product.objects.filter(category='JC')
  paintingCraft =Product.objects.filter(category='PC')
  return render(request, 'app/home.html', 
  {'bambooCraft':bambooCraft, 'metalCraft':metalCraft ,'juteCraft':juteCraft, 'paintingCraft':paintingCraft})

def home(request):
  # send_mail(
  #   'Testing Mail',
  #   'welcome to ecraft',
  #   'Khushalneware2003@gmail',
  #   ['sudheerneware@gmail.com'],
  #   fail_sliently = False,
  # )

  return render(request, 'app/home.html')

def payment(request):
  pay=Product.objects.all()
  return render(request, 'app/payment.html',{'pay':pay})

class ProductDetailView(View):
 def get(self,request ,pk):
  product =Product.objects.get(pk=pk)
  return render(request,'app/productdetail.html',{'product':product})
 
 
def cart(request):
  user=request.user
  product_id = request.GET.get('prod_id')
  product= Product.objects.get(id=product_id)
  Cart(user=user,product=product).save()
  
  if request.user.is_authenticated:
    user =request.user
    cart =Cart.objects.filter(user=user)
  
  return render(request, 'app/cart.html',{'carts':cart})
  
def showcart(request):
  if request.user.is_authenticated:
    user =request.user
    show =Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 50.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    if cart_product:
      for p in cart_product:
        tempamount = (p.quantity * p.product.price)
        amount += tempamount
        totalamount = amount + shipping_amount

      return render(request, 'app/show.html',{'carts':show, 'totalamount':totalamount,'amount':amount})
    else:
      return render(request,'app/empty.html')
  else:
    return redirect('/login')

  


def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
  if request.user.is_authenticated:
    op =OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'op':op})
  
  else:
    return render(request,'app/empty.html')
  

def remove(request):
  user=request.user
  ca=Cart.objects.filter(user=user)
  for c in ca:
    c.delete()
  return redirect("/show")

def remove1(request):
  user=request.user
  ca=OrderPlaced.objects.filter(user=user)
  for c in ca:
    c.delete()
  return redirect("/")

def payment_done(request):
  user=request.user
  car=Cart.objects.filter(user=user)
  for c in car:
    OrderPlaced(user=user,product=c.product,quantity=c.quantity).save()
    c.delete()
  return redirect("/")

def mobile(request):
 return render(request, 'app/mobile.html')

# def login(request):
#  return render(request, 'app/login.html')

# def register(request):
#  return render(request, 'app/register.html')

def checkout(request):
 return render(request, 'app/checkout.html')

def search(request):
    # results=Product.objects.all()
    query = request.GET.get('search')
    results = []

    if query:
        # Perform a search query on your Product model
        results = Product.objects.filter(title__icontains=query)
    context = {'results': results}

    return render(request , 'app/search.html', context)
    

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        data =User.objects.create_user(username=username,email=email,password=password1)
        messages.success(request,'congratulation ! registration successfully')
        data.save()
        return redirect('/register')
    return render(request,"app/register.html")
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Welcome To Ecraft website')
            return redirect('/')
                      
    return render(request,"app/login.html")

def logout(request):
  auth.logout(request)
  return redirect('/')

def profile(request):
  if request.user.is_authenticated:
    
    return render(request,'app/profile.html')
  else:
    return redirect('/login')
  


  
def shop(request):
    if request.method=='POST':
        username = request.POST['username']
        shopname = request.POST['shopname']
        craftname = request.POST['craftname']
        address = request.POST['address']
        city = request.POST['city']
        
        data =Shop.objects.create(username=username,shopname=shopname,craftname=craftname,address=address,city=city)
        data.save()
        return redirect('/')
    return render(request,"app/shop.html")



def profile_edit(request):
    if request.method=='POST':
        username = request.POST['username']
        gender = request.POST['gender']
        email = request.POST['email']
        address = request.POST['address']
        mobile_no = request.POST['mobile_no']
        
        data =Profile.objects.create(username=username,gender=gender,email=email,address=address,mobile_no=mobile_no)
        data.save()
        return redirect('/')
    return render(request,"app/profile_edit.html")


  

def category(request):
  return render(request,"app/category.html")


  
def aboutus(request):
  return render(request,"app/aboutus.html")


  
def ngo(request):
  return render(request,"app/Ngo.html")

def selling(request): 
  return render(request,"app/selling.html")


def shopview(request): 
  return render(request,"app/shopview.html")
  

def edit(request):
  return render(request,"app/profile_edit.html")


def design(request):
  return render(request,"app/design.html")

  

def orderhistory(request): 
  return render(request,"app/orderhistory.html")



  
def qr(request): 
  return render(request,"app/qr.html")




def contactus(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']

        data =Contactus.objects.create(username=username,email=email,address=address)
        data.save()
        return redirect('/')
    return render(request,"app/contactus.html")