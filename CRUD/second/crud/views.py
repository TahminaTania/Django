from django.shortcuts import render,HttpResponseRedirect
from .forms import Sregistration
from .models import user

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = Sregistration(request.POST )
        
        if fm.is_valid():
            N=fm.cleaned_data['name']
            E= fm.cleaned_data['email']
            P= fm.cleaned_data['password']
            reg =user(name=N,email=E,password=P)
            reg.save()
            fm = Sregistration() 
    else:
        fm = Sregistration()
    student = user.objects.all()               
    return render(request,'crud/addNshow.html',{
        'form':fm,
        'stud':student
        })

def delete(request,id):
    if request.method=='POST':
        new = user.objects.get(pk='id')  
        new.delete()
    return HttpResponseRedirect('/')
