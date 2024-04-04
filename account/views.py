from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.forms import  UserCreationForm
from .models import LoginForm,UserForm
from income.models import Income
from expense.models import Expense
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

def get_balance(request):
    uid=request.session.get("uid")
    incl=Income.objects.filter(user=uid)
    expl=Expense.objects.filter(user=uid)
    total_income=0
    total_expense=0
    for i in incl:
        total_income=total_income+i.income
    
    for i in expl:
        total_expense=total_expense+i.expense

    return total_income-total_expense


def home(request):
    context={"bal":get_balance(request)}
    return render(request,"home.html",context)

def adduser(request):
    if request.method=='POST':
        f=UserCreationForm(request.POST)
        f.save()
        return redirect("/")
    else:
        f=UserCreationForm()
        context={'form':f}
        return render(request,"adduser.html",context)

def login_view(request):
    if request.method=='POST':  
        uname=request.POST.get("username")
        passw=request.POST.get("password") 
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session["uid"]=user.id
            login(request,user)
            return redirect("/")
        else: 
            f=LoginForm
            context={'form':f}
            return render(request,"login.html",context)
    else:
        f=LoginForm
        context={'form':f}
        return render(request,"login.html",context)


def logout_view(request):
    logout(request)
    return redirect("/") 

def edit_profile(request):
    uid=request.session.get("uid")
    u=User.objects.get(id=uid)
    if request.method=='POST':
        f=UserForm(request.POST,instance=u)
        f.save()
        return redirect("/")
    else:
        f=UserForm(instance=u)
        context={'form':f}
        return render(request,"updateuser.html",context)