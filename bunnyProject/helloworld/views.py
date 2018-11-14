import requests
import random
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Name
from .forms import NameForm,UserTableForm

# Create your views here.
def getin(request):
    context = {'page_name': 'Login'}
    if request.method['POST']:
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
    return render(request,'login.html',context )

def userregister(request):
    form = UserTableForm()
    context = {'form': form,'page_name':'Register '}
    return render(request,'login.html',context )


def index(request):
    form = NameForm()
    if request.method == "POST":
        r = NameForm(request.POST)
        if r.is_valid():
            # print('Validation Succeess')
            r.save()
            redirect('blog')
    context = {'form':form}
    return render(request,'index.html',context)

def blog(request):
    colors_array = {'bg-primary','bg-secondary','bg-success','bg-danger','bg-warning'}
    form_list = Name.objects.order_by('-id')
    context = {'form_list':form_list,'colors_array':colors_array}
    return render(request,'blog_list.html',context)

def blog_details(request, blog_id):
    blog_detail = Name.objects.get(id=blog_id)
    context = {'blog_detail':blog_detail}
    print(blog_detail.name)
    return render(request,'blog_details.html',context)

def delete(request,name_id):
    Name.objects.filter(pk=name_id).delete()
    return redirect('blog')

def update(request, name_id):
    name_data =   Name.objects.get(id=name_id)
    form = NameForm(request.POST or None, instance=name_data)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form':form,'name_data':name_data}
    return render(request,'index.html',context )
def about(request,name_id):
   pass

