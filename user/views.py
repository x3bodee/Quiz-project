from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate , logout
from user.forms import RegistrationForm, UserAuthForm, UserUpdateForm
from user.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# if it's get request it's will just load the page if it's post then
# it's will create new user record 
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

# if it's get request it's will just load the page if it's post then
# it's will check if the user entered username and pass
# is correct then it's will login if not then it's 
# will not login
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

# get all user info and send it to profile
# page to presinte it to the user
def profile_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        context['profile'] = get_object_or_404(User, username=user)
        return render(request, 'profile.html', context)
    return redirect('login')

# this will logout if the user is logged in
@login_required(login_url='/user/login/')
def logout_view(request):
    logout(request)
    return redirect('home')

# this will open the open the update user data
# open the update page with the form 
@login_required(login_url='/user/login/')
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


