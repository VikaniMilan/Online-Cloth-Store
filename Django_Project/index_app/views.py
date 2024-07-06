from audioop import reverse
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from index_app.models import *
from product.models import *
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def index(request):
    newarrivalimg = NewArrival.objects.all()
    BrandImage = Brand.objects.all()
    data = {
        'slider' : newarrivalimg,
        'Brand' : BrandImage
    }
    return render(request, 'index.html', data)

def productList(request):
    if request.method == "POST":
        
        product = request.POST.get('productid')
        user = request.user.id
        current_datetime = datetime.datetime.now() 
        form_type = request.POST.get('form_type')

        if form_type == 'cart_form':
            obj = Cart(customer_id = user, product_id = product, order_date = current_datetime)
            obj.save()

        if form_type == 'wl_form': 
            obj = Wishlist(customer_id = user, product_id = product)
            obj.save()

        return render(request, 'product-list.html')

    else:
        context = {
            'product' : Product.objects.all(),
            'retailer' : Retailer.objects.all()
        }
    return render(request, 'product-list.html', context)

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    mydata = Cart.objects.all()
    product = Product.objects.all()
    bill = 0

    for obj in mydata:
        if obj.customer_id == request.user.id:
            for obj1 in product:
                if obj.product_id == obj1.id:
                    bill += obj1.price

    context = {
        'list' : mydata,
        'product_list' : product,
        'bill' : bill
    }
    return render(request, 'cart.html', context)

def wishlist(request):
    mydata = Wishlist.objects.all()
    product = Product.objects.all()

    context = {
        'list' : mydata,
        'product_list' : product,
    }
    return render(request, 'wishlist.html', context)

def checkout(request):
    return render(request, 'checkout.html')

def myAccount(request):
    obj = Address.objects.all()
    order = User_Order.objects.all()
    order_item = Order_Item.objects.all()
    product = Product.objects.all()
    contex = {
        'address' : obj,
        'orders' : order,
        'order_data' : order_item,
        'product' : product
    }
    return render(request, 'my-account.html', contex)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}.")
                return redirect("index")
            else: 
                messages.err or(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")

def addAddress(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        adr1 = request.POST['address1']
        adr2 = request.POST['address2']
        city = request.POST['city']
        dict = request.POST['district']
        state = request.POST['state']
        pin = request.POST['pincode']
        mobile = request.POST['mobile']
        user = request.user
        userid = user.id
        
        obj = Address(First_Name = fname, Last_Name = lname, AddressLine1 = adr1, AddressLine2 = adr2, City = city, District = dict, State = state, PinCode = pin, mobile = mobile, username_id = userid)
        
        obj.save()

        return redirect('my-account')
    
def addtocart(request):
    product = request.POST['productid']
    obj = Cart(customer_id = request.user.id, product_id = product)
    obj.save()
    return redirect(cart)

def addtowl(request):
    product = request.POST['productid']
    obj = Wishlist(customer_id = request.user.id, product_id = product)
    obj.save()
    return redirect(wishlist)

def remove(request):
    id = request.POST['cartid']
    member = Cart.objects.get(id=id)
    member.delete()
    return redirect(cart)

def additem(request, id):
    item = Wishlist.objects.get(id = id)
    obj = Cart(customer_id = request.user.id, product_id = item.product_id)
    obj.save()
    return redirect(wishlist)

def wlremove(request, id):
    item = Wishlist.objects.get(id = id)
    item.delete()
    return redirect(wishlist)

def men_category(request):
    product = Product.objects.filter(category = 'men')
    context = {
        'list' : product
    }
    return render(request, "men.html", context)

def women_category(request):
    product = Product.objects.filter(category = 'women')
    context = {
        'list' : product
    }
    return render(request, "women.html", context)

def order(request, bill):
    obj = User_Order(customer_id = request.user.id, )
    obj.save()
    order_id = obj.id

    cart_data = Cart.objects.all()
    for cartp in cart_data:
        if cartp.customer_id == request.user.id:
            add = Order_Item(Order_id_id = order_id, Product_id_id = cartp.product_id)
            add.save()

    return render(request, "index.html")