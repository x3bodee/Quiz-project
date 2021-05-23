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
    # home url
    path('' , views.home , name= "home" ),
    # quizlist url
    path('quiz/' , QuisListView.as_view() , name= "main-view" ),
    # my created quizez url
    path('myquizes/' , views.myquizes , name= "myquizes"),
    # open quiz url
    path('quiz/<pk>/' , quiz_view , name="quiz-view"),
    # delete quiz url
    path('delete_quiz/<pk>/' , views.deleteQuiz ,name = "delete_quiz") ,
    # save result url (used by ajax)
    path('quiz/<pk>/save/' , save_quiz_view , name="save-view"),
    # view result of the quiz (used by ajax)
    path('quiz/<pk>/data/' , quiz_data_view , name="quiz-data-view"),
    # create quiz with it's questions 
    path('addquiz/' , views.addquiz , name= "addquiz" ),
    # path('addquestion/' , views.addquestion , name= "addquestion" ),
    # path('addAnswers/' , views.addAnswers , name= "addAnswers" ),
    # path('quizResult/' , views.quizResult , name= "quizResult" ),
   
    
    
]