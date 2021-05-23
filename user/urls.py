from django.contrib import auth
from django.urls import path
from django.contrib.auth import views as as_view ,views as auth_views
from user import views as user_views


urlpatterns = [
    # login url
    path('login/' , user_views.login_view ,name="login"),
    # logout url
    path('logout/' , user_views.logout_view , name= "logout"), 
    # signup url
    path('signup/' , user_views.signup_view ,name="signup"), 
    # profile url
    path('profile/' , user_views.profile_view ,name="profile"),
    # update url
    path('update/' , user_views.update_view ,name="update"),
    # change password url
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name="password_change.html" ),name='password_change'),
    # change password done url
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done2.html"),name='password_change_done'),
    
]