from django.shortcuts import render , HttpResponse , redirect
from django.http import JsonResponse
from datetime import datetime
from .models import Quiz
from django.views.generic import ListView

# Create your views here.
def home(request):
 
    return  render(request,'home.html' , {}) 


class QuisListView(ListView):
    model=Quiz
    template_name='quiz/quizlist.html'

def quiz_view(request , pk):
    
    try:
        quiz=Quiz.objects.get(pk=pk)
    except Exception:
        return HttpResponse("error")
    
    return render(request , 'quiz/show.html' ,
    {   
    "obj" : quiz
    } )


def addquiz(request):
     
    return  render(request,'teachers/addQuiz.html' , {}) 

def addquestion(request):
     
    return  render(request,'teachers/addQuestion.html' , {}) 


def startquiz(request):
    
    return  render(request,'students/startQuiz.html' , {}) 

def myquizes(request):
    
    return  render(request,'Quiz/myquizes.html' , {}) 

def quizResult(request):
    
    return  render(request,'teachers/studentResult.html' , {}) 


def addAnswers(request):
    
    return  render(request,'teachers/addAnswers.html' , {}) 


    

