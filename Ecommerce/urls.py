
from django.contrib import admin
from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HOME, name = 'home' ),
    path('base/', views.BASE, name = 'base' ),
    path('product/', views.PRODUCT, name = 'product' ), 
    path('about/', views.ABOUT, name = 'about' ), 
    path('contact/', views.CONTACT, name = 'contact' ),
    path('search/', views.SEARCH, name = 'search' ),  
    path('singleproduct/<str:id>', views.SINGLPRO, name = 'singleproduct' ),  
    
    path('register/', views.HandleRegister, name = 'register' ),
    path('login/', views.HandleLogin, name = 'login' ), 
    path('logout/', views.HandleLogout, name = 'logout' ),
    
    # path('cart/cart_detail/', views.CART, name = 'cart_detail' ), 
    
    #cart here
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
    path('cart/checkout/',views.CHECKOUT,name='checkout'),
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
