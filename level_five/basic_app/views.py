from django.shortcuts import render,redirect
from basic_app.forms import UserForm,UserProfileInfoForm

#Login code goes here
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    context ={}
    return render(request,'basic_app/index.html',context)

def register(request):
    registered = False
    context = {'registered':registered}
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_profile = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile.save(commit=False)
            profile.user = user
            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']
            profile.save()

            registered = True
        else:
            print(user_form.errors,user_profile.errors)
    else:
        user_form = UserForm()
        user_profile = UserProfileInfoForm()
    context = {'user_form':user_form,'user_profile':user_profile,'registered':registered}
    return render(request,'basic_app/registration.html',context)



def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return  HttpResponseRedirect(reverse('basic_app:index'))
            else:
                return HttpResponse("Account Not Active..!")
        else:
            print("Someone trying to login and Failed!")
            print("Username : {} and Password : {}".format(username,password))
            return HttpResponse("Invalid Login Details")
    else:
        return render(request,'basic_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic_app:user_login'))

@login_required
def special(request):
    return render(request,'basic_app/special.html')
