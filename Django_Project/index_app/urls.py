from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('', views.index, name = 'index'),
    path('product-list', views.productList, name = 'product-list'),
    path('contact', views.contact, name = 'contact'),
    path('usercart', views.cart, name = 'usercart'),
    path('wishlist', views.wishlist, name = 'wishlist'),
    path('checkout', views.checkout, name = 'checkout'),
    path('login', views.login_request, name = 'login'),
    path('my-account', views.myAccount, name = 'my-account'),
    path('register', views.register_request, name = 'register'),
    path('logout', views.logout_request, name = 'logout'),
    path('addAddress', views.addAddress, name = 'addAddress'),
    path('product-list/addtocart', views.addtocart, name = 'addtocart'),
    path('product-list/addtowl', views.addtowl, name = 'addtowl'),
    path('usercart/remove', views.remove, name='remove'),
    path('wishlist/additem/<id>', views.additem, name='additem'),
    path('wishlist/remove/<id>', views.wlremove, name='wlremove'),
    path('men-category', views.men_category, name = 'men_category'),
    path('women-category', views.women_category, name = 'women_category'),
    path('usercart/order/<int:bill>', views.order, name = 'order')
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 