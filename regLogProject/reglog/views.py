from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from  django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,'reglog/login.html',{'message':None})
    context = {'user':request.user}
    return render(request,'reglog/user.html',context)

def user_register(request):
    pass

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username'] 
            password = request.POST['password']
            print(username)
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,"reglog/login.html",{'message':'invalid Credintials'})
        return render(request,'reglog/login.html',{'message':None})
    else:
        return HttpResponseRedirect(reverse('index'))
def user_logout(request):
    logout(request)
    return render(request,"reglog/login.html",{'message':'Logout Successfull'})
