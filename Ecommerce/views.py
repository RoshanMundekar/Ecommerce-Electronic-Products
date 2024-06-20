from django.shortcuts import redirect,render
from store_app.models  import Product,Categories,Filter_Price,Color,Brand,Contact_us
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from cart.cart import Cart



def BASE(request):
    return render(request,'Main/base.html')


def PRODUCT(request):
    product= Product.objects.all()
    categories=Categories.objects.all()
    filter_price=Filter_Price.objects.all()
    color=Color.objects.all()
    brand1=Brand.objects.all()
    
    CATID =request.GET.get("categories")
    FILTER_PRICE =request.GET.get("filtter_price")
    BRAND =request.GET.get("brand")
    ATOZID =request.GET.get("ATOZ")
    ZTOAID =request.GET.get("ZTOA")
    
    LOWTOHIGH =request.GET.get("PRICELTH")
    HIGHTOLOW =request.GET.get("PRICEHTL")
    
    NEW =request.GET.get("NEW")
    OLD =request.GET.get("OLD")
    
    print(FILTER_PRICE)
    if CATID:
        product= Product.objects.filter(categories=CATID,status="Publish")
    elif FILTER_PRICE:
        product= Product.objects.filter(filter_price=FILTER_PRICE,status="Publish")
    elif BRAND:
        product= Product.objects.filter(brand=BRAND,status="Publish")    
    elif ATOZID:
        product= Product.objects.filter(status="Publish").order_by("name") 
    elif ZTOAID:
        product= Product.objects.filter(status="Publish").order_by("-name")         
    elif LOWTOHIGH:
        product= Product.objects.filter(status="Publish").order_by("price")             
    elif HIGHTOLOW:
        product= Product.objects.filter(status="Publish").order_by("-price") 
    elif NEW:
        product= Product.objects.filter(status="Publish",condition="New")
    elif OLD:
        product= Product.objects.filter(status="Publish",condition="Old")                        
            
    else:
        product= Product.objects.filter(status="Publish") 
        

    context={
        "product":product,
        "categories":categories,
        "filter_price":filter_price,
        "color":color,
        "brand1":brand1
    }
    return render(request,'Main/product.html',context)

def HOME(request):
    product= Product.objects.filter(status="Publish")
    context={
        "product":product
    }

    return render(request,'Main/index.html',context)

def ABOUT(request):

    return render(request,'Main/about.html')


def CONTACT(request):
    if request.method =="POST":
        name =request.POST.get("name")
        email =request.POST.get("email")
        subject =request.POST.get("subject")
        message =request.POST.get("message")
        # print(name,email,subject,message)
        contact = Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        contact.save()
        return redirect('home')
    return render(request,'Main/contact.html')

def SEARCH(request):
    QUERY =request.GET.get("query")
    product= Product.objects.filter(name__icontains=QUERY)
    context={
        "product":product
    }
    return render(request,'Main/search.html',context)

def SINGLPRO(request,id):
    prod= Product.objects.filter(id=id).first()
    context={
        "prod":prod
    }
    
    return render(request,'Main/singleproduct.html',context)


def HandleRegister(request):
    if request.method =="POST":
        username =request.POST.get("username")
        first_name =request.POST.get("first_name")
        Last_name =request.POST.get("Last_name")
        email =request.POST.get("useremail")
        pass1 =request.POST.get("pass1")
        pass2 =request.POST.get("pass2")
        
        print(username,first_name,Last_name,email,pass1,pass2)
        
        customer=User.objects.create_user(username,email,pass1)
        customer.first_name = first_name
        customer.last_name = Last_name
        customer.save()
        return redirect('register')
        
    return render(request,'Registration/auth.html')


def HandleLogin(request):
    if request.method =="POST":
        username =request.POST.get("username")
        password =request.POST.get("password")
        print(username,password)
        user = authenticate( request , username = username, password = password)
        
        if user  is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'Registration/auth.html')
        
    return render(request,'Registration/auth.html') 
            
            
        
def HandleLogout(request):
    logout(request)
    # return redirect('home')
    return render(request,'Main/index.html')


def CHECKOUT(request):
    
    return render(request,'Cart/checkout.html')



#cart here

@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    return render(request, 'Cart/cart_detail.html')
        