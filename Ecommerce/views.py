from django.shortcuts import redirect,render
from store_app.models  import Product,Categories,Filter_Price,Color,Brand



def BASE(request):
    return render(request,'Main/base.html')


def PRODUCT(request):
    product= Product.objects.all()
    categories=Categories.objects.all()
    filter_price=Filter_Price.objects.all()
    color=Color.objects.all()
    brand1=Brand.objects.all()

    context={
        "product":product,
        "categories":categories,
        "filter_price":filter_price,
        "color":color,
        "brand1":brand1
    }
    return render(request,'Main/product.html',context)

def HOME(request):
    product= Product.objects.all()
    context={
        "product":product
    }

    return render(request,'Main/index.html',context)