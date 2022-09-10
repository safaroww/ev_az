from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout

# Create your views here.

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('sale:home')
        
     
    return render(request, 'seller/login.html', context={
        'form': form
    })

def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller:login')
    return render(request, 'seller/register.html', context={
        'form': form
    })
    
    
def logout_handler(request):
    logout(request)
    return redirect('seller:login')


def profile(request):
    form = UserChangeForm(instance=request.user)
    if request.method == 'POST':
        form = UserChangeForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.get_full_path())
    return render(request, 'seller/profile.html', context={
        'form': form
    })