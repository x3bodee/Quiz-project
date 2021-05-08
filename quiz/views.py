from django.shortcuts import render

# Create your views here.
def home(request):
 
    return  render(request,'home.html' , {}) 

def quizlist(request):
     
    return  render(request,'students/quizlist.html' , {}) 

def addquiz(request):
     
    return  render(request,'teachers/addQuiz.html' , {}) 

def addquestion(request):
     
    return  render(request,'teachers/addQuestion.html' , {}) 


def startquiz(request):
    
    return  render(request,'students/startQuiz.html' , {}) 

def updatequiz(request):
    
    return  render(request,'Quiz/updateQuiz.html' , {}) 

