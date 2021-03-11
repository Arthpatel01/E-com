from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Contact, Orders
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def index(request):
    products = Product.objects.all()
    
    params = {'product': products}
    return render(request, 'shop\index.html', params)

def about(request):
    return render(request, "shop\s_about.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        help1 = request.POST.get('help', '')

        cont = Contact(name=name, email=email, phone=phone, help1=help1)
        cont.save()
        messages.info(request, 'Your Problem is submited. Thank You!')
    return render(request, 'shop\contact_us.html')

def tracker(request):
    return HttpResponse("This is shop tracker")

def search(request):
    return HttpResponse("This is shop search")

def productview(request, myid):

    product = Product.objects.filter(id=myid)
    
    return render(request, "shop\prodview.html", {'product':product})

def checkout(request, id_b):
    product = Product.objects.filter(id=id_b)
    if request.method=='POST':
        name = request.POST.get('name_o', '')
        email = request.POST.get('email_o', '')
        phone = request.POST.get('phone_o', '')
        address = request.POST.get('add_o', '') + ", " + request.POST.get('add_o_2', '')
        city = request.POST.get('city_o', '')
        state = request.POST.get('state_o', '')
        zipcode = request.POST.get('zip_o', '')
        quantit = request.POST.get('quant', '')
        orderdate = datetime.today()
        for p in product:
            prod_id = id_b
            prod_name = p.product_name
            prod_price = p.price
            total = int(prod_price) * int(quantit)

        order = Orders(name=name, email=email, phone=phone, address=address, city=city, state=state, zipcode=zipcode, order_date=orderdate, prod_id=prod_id, prod_name=prod_name, prod_price=prod_price, quantity=quantit, total_price=total )
        order.save()

    return render(request, 'shop\checkout.html', {'product':product})


def handleSignup(request):
    if request.method == 'POST':
        email = request.POST['semail']
        fname = request.POST['sf_name']
        lname = request.POST['sl_name']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #Check:----
        if pass1 != pass2:
            print('Error pass not match')
            messages.error(request, "Password Do Not Match!!!!")
            return redirect('ShopHome')

        #User Creatingggg....
        myuser = User.objects.create_user(email, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Shopping Bazaar account has been created successfully.")

        return redirect('ShopHome')


    else:
        return HttpResponse('404 -- Not Found')        


def handleLogin(request):
    if request.method == 'POST':
         lemail = request.POST['lemail']
         lpass = request.POST['lpass']

         user = authenticate(username=lemail, password=lpass)
         if user is not None:
             login(request, user)
             messages.success(request, "Successfully Log In")
             return redirect('ShopHome')
         else:
             messages.error(request, "Invalid Email or Password!!, Please try again.")    
             return redirect('ShopHome')
    else:
        return HttpResponse('404 --Login Error redirect please.')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Log Out.")
    return redirect('ShopHome')