from django.urls import path
from quiz import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('' , views.home , name= "home" ),
    path('' , views.quizlist , name= "quizlist" ),
]