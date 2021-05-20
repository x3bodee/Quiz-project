from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate , logout
from user.forms import RegistrationForm, UserAuthForm, UserUpdateForm
from user.models import User
from django.contrib import messages




def signup_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            context['registration_form'] = form
    else: #GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'signup.html', context)

def login_view(request):
    context = {}
    user =request.user
    if user.is_authenticated:
        messages.add_message(request,messages.SUCCESS,"loggined succseefuly ")
        return redirect('home')
    
    if request.POST:
        form =UserAuthForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate( username=username, password=password )

            if user:
                login(request, user)
                return redirect('home')

    else:
        form = UserAuthForm()
    
    context['login_form'] = form
    return render(request, 'login.html', context)

def profile_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        context['profile'] = get_object_or_404(User, username=user)
        return render(request, 'profile.html', context)
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('home')

def update_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        context={'u_form': u_form}



    
    return render(request, 'update.html', context)

def resetpass_view(request):
    
    
    
    return render(request, 'password_change.html')
 
