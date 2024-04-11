from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# from . models import U

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Id exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,last_name=last_name,first_name=first_name,email=email,password=password)
                user.save()
                return redirect('login')
        else :
            messages.info(request,"Password and Confirm Password should be same")
            return redirect('register')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def log_in(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid Credentials")
            return redirect("login")
    return render(request,'login.html')

