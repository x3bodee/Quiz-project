from django.urls import path
from quiz import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('' , views.home , name= "home" ),
    path('quizlist/' , views.quizlist , name= "quizlist" ),
    path('startquiz/' , views.startquiz , name= "startquiz" ),
    path('addquiz/' , views.addquiz , name= "addquiz" ),
    path('addquestion/' , views.addquestion , name= "addquestion" ),
    path('updatequiz/' , views.updatequiz , name= "updatequiz" ),
]