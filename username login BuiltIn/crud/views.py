#from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import Sregistration,Uregistration
from .models import user
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.



def RegForm(request):
    form = Uregistration()
    if request.method == 'POST':
        form = Uregistration(request.POST)
        
        if form.is_valid():
            form.save()
            New_user=form.cleaned_data.get('first_name')
            messages.success(request,'Account Was created for  ' +New_user)
            return redirect('log')


    
    return render(request, 'crud/reg.html',{
        'form':form
    })



def LogIn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        person= authenticate(request, username=username, password=password)
        if person is not None:
            login(request,person)
            return redirect('add')
        else:
            messages.info(request, 'Username or password is incorrect')


    return render(request,'crud/login.html',{

    })    

def logOut(request):
    logOut(request)

    return redirect('log')

def add_show(request):
    if request.method == 'POST':
        fm = Sregistration(request.POST)
        student = user.objects.all()
        

        if fm.is_valid():
            N = fm.cleaned_data['name']
            E = fm.cleaned_data['email']
            P = fm.cleaned_data['password']           
            reg = user(name=N, email=E, password=P)
            reg.save()               
    else:
        fm = Sregistration()   
    student = user.objects.all()
    return render(request, 'crud/addNshow.html', {
        'form': fm,
        'stud': student
    })


def update(request, id):
    if request.method == 'POST':
        new = user.objects.get(pk=id)
        up = Sregistration(request.POST, instance=new)
        if up.is_valid():
            up.save()
    else:
        new = user.objects.get(pk=id)
        up = Sregistration(instance=new)

    return render(request, 'crud/update.html', {
        'form': up,
        'id': id
    })


def delete(request, id):
    if request.method == 'POST':
        new = user.objects.get(pk=id)
        new.delete()
    return HttpResponseRedirect('/')
