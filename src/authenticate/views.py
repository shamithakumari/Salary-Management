from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, accountant_only
from .models import Employee
from salary.views import details
# Create your views here.

@unauthenticated_user
def home(request):
    return render(request, "authenticate/home.html", {})

@unauthenticated_user
def signup(request):
    if request.method == "POST":
        eid = request.POST['eid']
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phno']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=eid):
            messages.error(request, "EID already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(eid)>20:
            messages.error(request, "EID must be under 20 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not eid.isalnum():
            messages.error(request, "EID must be Alpha-Numeric!!")
            return redirect('signup')
        
        myuser = User.objects.create_user(username=eid,first_name=fname,last_name=lname,email=email,password=pass1)
        # myuser.first_name = fname
        # myuser.last_name = lname
        # myuser.email = email
        # myuser.is_active = False
        # myuser.is_active = False
        emp = Employee(myuser)
        emp.userid=eid
        emp.address = address
        emp.phoneno = phone
        myuser.save()
        emp.save()
        messages.success(request, "Your Account has been created succesfully!!")

        return redirect('signin')
    return render(request, "authenticate/signup.html", {})

@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        eid = request.POST.get('eid')
        pass1 = request.POST.get('pass')
        # password = make_password('pass1')
        user = authenticate( username=eid, password=pass1)
        # print('User request')
        
        if user is not None:
            print('User request2')
            login(request, user)
            fname = user.first_name
            # lname = user.last_name
            #messages.success(request, "Logged In Sucessfully!!")
            # return render(request, "authenticate/index.html",{"fname":fname})
            return redirect('details')
        else:
            messages.error(request, "Invalid login")
            return render(request, "authenticate/signin.html", {})
    
    return render(request, "authenticate/signin.html", {})

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return render(request, "authenticate/signin.html", {})

@login_required(login_url='signin')
def index(request):
    return render(request, "authenticate/index.html", {})

@login_required(login_url='signin')
@accountant_only
def accountant_index(request):
    return render(request, "authenticate/a_index.html", {})

