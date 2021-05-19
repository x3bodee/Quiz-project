from django.shortcuts import render , HttpResponse , redirect
from django.http import JsonResponse
from datetime import datetime
from .models import Quiz
from django.views.generic import ListView
from question.models import Answer, Question
from result.models import Result

# Create your views here.
def home(request):
 
    return  render(request,'home.html' , {}) 

#show all quizes

class QuisListView(ListView):
    model=Quiz
    template_name='quiz/quizlist.html'
#show quizes that user create
def myquizes(request): 

    myQui = Quiz.objects.all()
    return render(request , 'quiz/myquizes.html' , 
    {"ob" : myQui  })

#start quiz
def quiz_view(request , pk):
    
    try:
        quiz=Quiz.objects.get(pk=pk)
    except Exception:
        return HttpResponse("error")
    
    return render(request , 'quiz/startQuiz.html' ,
    {   
    "obj" : quiz
    } )


    
#shows results
def results_view(request):
    
    try:
        result=Result.objects.all()
    except Exception:
        return HttpResponse("error")
    
    return render(request , 'quiz/results.html' ,
    {   
    "results" : result
    } )


    
# this view for sending data 
def quiz_data_view (request ,pk):
    quiz=Quiz.objects.get(pk=pk)
    questions =[]
    for q in quiz.get_questions():
        answers=[]
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q):answers})
    return JsonResponse({
        'data' : questions,
        'time' : quiz.time,
    })
 #save students answers   
def save_quiz_view(request,pk):
    #print(request.POST)
    if request.is_ajax():
        questions=[]
        data=request.POST
        data_=dict(data.lists())
        #print(type(data))
        #print(type(data_))
        data_.pop('csrfmiddlewaretoken')
        for k in data_.keys():
            print('key: ', k)
            question=Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user=request.user
        quiz=Quiz.objects.get(pk=pk)

        score = 0
        multipler = 100/ quiz.number_of_question
        results =[]
        correct_answer= None 
        for q in questions:
            a_selected =request.POST.get(q.text)

            if a_selected !="":
                question_answers=Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected== a.text:
                        if a.correct:
                            score +=1
                            correct_answer= a.text
                    else:
                        if a.correct:
                            correct_answer=a.text
                results.append({str(q):{'correct_answer': correct_answer, 'answered': a_selected }})
            else:
                results.append({str(q):'Not answered'})
        score_ =score * multipler 
        Result.objects.create(quiz=quiz,user=user,score=score_)

        if score_ >= quiz.score_to_pass:
            return JsonResponse({'passed':True,'score':score_ ,'results': results})
        else:
            return JsonResponse({'passed': False ,'score':score_ ,'results': results})





#delete quiz
def deleteQuiz(request , pk):
    quiz=Quiz.objects.get(id=pk)
    quiz.delete()
    context= {'item':quiz}
    return redirect('/myquizes' )


def convertToArr(obj):
    dele=["csrfmiddlewaretoken","name","time","ispublic","difficulty","type"]
    arr=[]
    for item in obj:
        print(item)
        if item not in dele:
            arr.append(item+" - "+obj[item])
    return arr

#['q-1$$TorF - 1+1=2', 'q-1-answer - true', 'q-2 - 5*5',
# 'q-2-answer - 25', 'ch-2 ### q-2 - 22', 'ch-3 ### q-2 - 23', 
# 'ch-4 ### q-2 - 24']

def covertStrToQueries(arr):
    for item in arr:
        subarr = item.split(" - ")
        if subarr[0]== "q-":
            print()
        print(subarr)
    print("Quistion : ")
    print("choiceis : ")
    print(arr)


def addquiz(request):
    
    if request.POST:
        print("POST")
        obj=request.POST
        name = obj["name"]
        time = obj["time"]
        dif = obj["difficulty"]
        public=""
        if obj["ispublic"] == "public":
            public = obj["ispublic"]
        arr =convertToArr(obj)
        print(arr)
        covertStrToQueries(arr)
        # print(request.POST.remove(name))
        
        

    print("done :)")
    return  render(request,'quiz/newquiz.html' , {}) 

def addquestion(request):
     
    return  render(request,'teachers/addQuestion.html' , {}) 


def startquiz(request):
    
    return  render(request,'students/startQuiz.html' , {}) 



def quizResult(request):
    
    return  render(request,'teachers/studentResult.html' , {}) 


def addAnswers(request):
    
    return  render(request,'teachers/addAnswers.html' , {}) 


    

