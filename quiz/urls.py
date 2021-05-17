from django.urls import path
from quiz import views 
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    QuisListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    
)


urlpatterns = [
    path('' , views.home , name= "home" ),
    path('quiz/' , QuisListView.as_view() , name= "main-view" ),
    path('myquizes/' , views.myquizes , name= "myquizes"),
    #path('quiz/new/' , views.new_quiz , name='new_quiz'),
    path('quiz/<pk>/' , quiz_view , name="quiz-view"),
    
    path('delete_quiz/<pk>/' , views.deleteQuiz ,name = "delete_quiz") ,

    path('quiz/<pk>/save/' , save_quiz_view , name="save-view"),
    path('quiz/<pk>/data/' , quiz_data_view , name="quiz-data-view"),

    path('startquiz/' , views.startquiz , name= "startquiz" ),
    path('addquiz/' , views.addquiz , name= "addquiz" ),
    path('addquestion/' , views.addquestion , name= "addquestion" ),
    path('addAnswers/' , views.addAnswers , name= "addAnswers" ),
    path('quizResult/' , views.quizResult , name= "quizResult" ),
   
    
    
]