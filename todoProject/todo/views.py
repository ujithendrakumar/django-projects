from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import requests
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
    todo_list = Todo.objects.order_by('id')


    if request.method == 'POST':
        form = TodoForm(request.POST)
        form.save()
    form = TodoForm()

    context  = {'todo_list':todo_list ,'form':form}
    return render(request,'todo/index.html',context)

@require_POST
def add(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(name=request.POST['name'])
        new_todo.save()

    # print(request.POST['name'])
    return redirect('index')

def about(request):
    return HttpResponse('test')

def complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def completeDelete(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def completeAll(request):
    Todo.objects.all().delete()
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})