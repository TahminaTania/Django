from django.shortcuts import render
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import Uregistration
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def RegForm(request):
    form = Uregistration()
    if request.method == 'POST':
        form = Uregistration(request.POST)
        if form.is_valid():
            form.save()
            NewUser = form.cleaned_data.get('username')
            messages.success(
                request, 'An Account just created for- ' + NewUser + ' Please log in')
            return redirect('log')
    return render(request, 'Custom/reg.html', {
        'form': form
    })