from django.contrib import auth
from django.urls import path
from django.contrib.auth import views as as_view ,views as auth_views
from user import views as user_views




urlpatterns = [
    path('login/' , user_views.login_view ,name="login"),
    path('logout/' , user_views.logout_view , name= "logout"), 
    path('signup/' , user_views.signup_view ,name="signup"), 
    path('profile/' , user_views.profile_view ,name="profile"),
    path('update/' , user_views.update_view ,name="update"),
    # change password urls
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name="password_change.html" ),name='password_change'),
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"),name='password_change_done'),
    
]