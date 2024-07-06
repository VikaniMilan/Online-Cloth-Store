from pyexpat.errors import messages
from django.shortcuts import redirect, render
from product.models import *
from django.contrib.auth.hashers import check_password
from django.core.files.storage import FileSystemStorage

def retailerlogin(request):
    if request.method == "POST":
        cid = request.POST['cid']
        pwd = request.POST['pwd']

        gobj = Retailer.objects.all()

        for obj in gobj:
            if obj.cid == cid:
                if obj.password == pwd:
                    request.session['companyid'] = obj.cid
                    request.session['id'] = obj.id
                    
                    return redirect('add_item')

                else:
                    context = {
                        'msg' : "Username or Password is wrong"
                    }
                    return render(request, 'retailerlogin.html', context)

        context = {
            'msg' : "Username is not Registered."
        }
        return render(request, 'retailerlogin.html', context)
                
    else:
        
        return render(request, 'retailerlogin.html') 

def retailerregistration(request):
    if request.method == "POST":
        cid = request.POST['cid']
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        cmobile = request.POST['cmobile']
        pwd = request.POST['pwd']
        conpwd = request.POST['conpwd']

        if pwd == conpwd:
            obj = Retailer(cid = cid, cname = cname, password = pwd, companyemail = cemail, companymobile = cmobile)
            obj.save()

            return redirect('retailerlogin')

        else:
            return render(request, 'retailerregistration.html', {'msg' : "Password and Confirm password are not same"})
    else:
        return render(request, 'retailerregistration.html')

def add_item(request):
    if request.method == "POST":
        rid = request.session['id']
        pname = request.POST['pname']
        price = request.POST['price']
        category = request.POST['cat']
        img = request.FILES['image']

        obj = Product(name = pname, price = price, category = category, image = img, retailer_id = rid)
        obj.save()
        context = {
            'msg' : "item added successfully"
        }
        return render(request, 'retailer_add_item.html', context)
    else:
        return render(request, 'retailer_add_item.html')
    