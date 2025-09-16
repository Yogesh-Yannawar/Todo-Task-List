from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import TodoModel
# Create your views here.

def signup_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pswd=request.POST.get('password')
        user=User.objects.create_user(username=uname,password=pswd,email=email)
        user.save()
        return redirect('login')
    return render(request,'signup_temp.html')

def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pswd=request.POST.get('password')
        print(uname,pswd)
        user=authenticate(request,username=uname,password=pswd)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return render(request,'login_temp.html',context={'msg':'Invalid Credentials'})
    return render(request,'login_temp.html')

@login_required
def dashboard_view(request):
    if request.method=='POST':
        title=request.POST.get('title')
        obj=TodoModel.objects.create(title=title,user=request.user)
        res=TodoModel.objects.filter(user=request.user).order_by('-date')
        return render(request,'dashboard.html',context={'res':res})
    res=TodoModel.objects.filter(user=request.user).order_by('-date')
    return render(request,'dashboard.html',context={'res':res})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def update_task(request,sno):
    obj=TodoModel.objects.get(sno=sno)
    if request.method=='POST':
        title=request.POST.get('title')
        if title:
            obj.title=title
            obj.save()
        return redirect('dashboard')
    return render(request,'update.html',context={'obj':obj})

def delete_task(request,sno):
    obj=TodoModel.objects.get(sno=sno)
    obj.delete()
    return redirect('dashboard')
    

    
        
    

    