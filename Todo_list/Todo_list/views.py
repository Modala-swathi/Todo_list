from django.shortcuts import render,redirect
 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login ,logout as auth_logout
from .models import Task
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return redirect('/login')
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('todo')
    return render(request,'login.html')

@login_required(login_url='/login')
def todo(request):
    if request.method=='POST':
        task=request.POST.get('task')
        obj=Task(task=task,user=request.user)
        obj.save()
        tasks=Task.objects.filter(user=request.user).order_by('-date')
        return render(request, 'todo.html',{'tasks':tasks})
    tasks=Task.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html',{'tasks':tasks})

@login_required(login_url='/login')
def edit_task(request,srno):
    if request.method=='POST':
        task=request.POST.get('task')
        obj=Task.objects.get(srno=srno)
        obj.task=task
        obj.save()
        tasks=Task.objects.filter(user=request.user).order_by('-date')
        return redirect('todo')
    obj=Task.objects.get(srno=srno)
    return render(request, 'edit_task.html',{'Task':obj}) 

@login_required(login_url='/login')
def delete_task(request,srno):
    obj=Task.objects.get(srno=srno)
    obj.delete() 
    return redirect('todo') 
def logout(request):
    auth_logout(request)
    return redirect('/login')