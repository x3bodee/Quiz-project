from django.shortcuts import render

# Create your views here.
def home(request):
 
    return  render(request,'home.html' , {}) 

def quizlist(request):
     
    return  render(request,'quiz/quizlist.html' , {}) 

def startquiz(request):
    
    return  render(request,'startQuiz/startQuiz.html' , {}) 