from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
from user.forms import RegistrationForm, UserAuthForm


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

def logout_view(request):
    logout(request)
    return redirect('home')
