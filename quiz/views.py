from django.shortcuts import render , HttpResponse , redirect
from django.http import JsonResponse
from datetime import datetime
from .models import Quiz
from django.views.generic import ListView
from question.models import Answer, Question
from result.models import Result
from quiz.models import Quiz
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return  render(request,'home.html' , {}) 

#show all quizes
class QuisListView(ListView):
    model=Quiz
    template_name='quiz/quizlist.html'


@login_required(login_url='/user/login/')
#show quizes that user create
def myquizes(request): 
    user=request.user
    myQui = Quiz.objects.filter(created_by=user)
    return render(request , 'quiz/myquizes.html' , 
    {"ob" : myQui  })

#start quiz
@login_required(login_url='/user/login/')
def quiz_view(request , pk):
    
    quiz=Quiz.objects.get(pk=pk)
    counter = Result.objects.filter(quiz=pk,user=request.user.id).count()
    #result=Result.objects.get(pk=pk)
    print(quiz.quiz_type)
    if quiz.quiz_type==True:
        return render(request , 'quiz/startQuiz.html' ,
        {   
        "obj" : quiz
        } )
    elif  quiz.quiz_type==False:
        if counter > 0 :
            result = Result.objects.get(quiz=pk,user=request.user.id)
            return render(request , 'quiz/private.html' ,
            {   
                "obj" : quiz,
                "resutl":result,
            } )
        else:
            return render(request , 'quiz/startQuiz.html' ,
        {   
        "obj" : quiz
        } )
        
@login_required(login_url='/user/login/')
def quiz_data_view (request ,pk):
    questions =[]
    for q in quiz.get_questions():
        answers=[]
        for a in q.get_answers():
            answers.append(a.text)
            # print(a.text)
        # print("q.get_answers")
        # print(answers)
        questions.append({str(q):answers})
    return JsonResponse({
        'data' : questions,
        'time' : quiz.time,
    })
    
# this view for sending data 
@login_required(login_url='/user/login/')
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

@login_required(login_url='/user/login/')
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
        print("the count of the ruselt :")
        # print(Result.objects.filter(quiz=quiz.id,user=user.id).count())
        if Result.objects.filter(quiz=quiz.id,user=user.id).count() > 0:
            print('there is user')
            Result.objects.filter(quiz=quiz.id,user=user.id).delete()
            print("old score is deleted")
            Result.objects.create(quiz=quiz,user=user,score=score_)
            print("the score is replaced")
        else:
            print('there is no old score')
            Result.objects.create(quiz=quiz,user=user,score=score_)
        if score_ >= quiz.score_to_pass:
            return JsonResponse({'passed':True,'score':score_ ,'results': results})
        else:
            return JsonResponse({'passed': False ,'score':score_ ,'results': results})


#delete quiz
@login_required(login_url='/user/login/')
def deleteQuiz(request , pk):
    quiz=Quiz.objects.get(id=pk)
    quiz.delete()
    context= {'item':quiz}
    messages.add_message(request,messages.SUCCESS,"quiz deleted ")
    return redirect('/myquizes' )


# /////////////////////////////////////////////////
# arr[0].split(" - ")[1]

# ['q-1$$TorF - 1+1=2', 'q-1-answer - true', 
# 'q-2$$MCQ - 1+2', 'q-2-answer - 3', 'ch-2 ### q-2 - 4',
#  'ch-3 ### q-2 - 2']

# answer : q-2-answer = 3
# choicess : ### q-2 = 2 ,

# solit by $$ for Question type
# split by  ###  for choice 
# split by answer -  for answer of Question
# split by  -  for the value

def convertToArr(obj):
    dele=["csrfmiddlewaretoken","name","time","ispublic","difficulty","type"]
    arr=[]
    for item in obj:
        # print(item)
        if item not in dele:
            el={
                "item":item,
                "value":obj[item],
                "flag":False,
                }
            arr.append(el)
    return arr

def isQuestion(item):
    if "$$" in item:
        print("this is question")
        return True
    return False

def isChoice(item):
    if " ### " in item:
        print("this is Choice")
        return True
    return False

def retAnswer(arr,q,flag=True):
    # search for answer of this question
    ttt=""
    if q != -1:
        ttt= q+"-answer"
        print(ttt)
    for el in arr:
        if ttt in el["item"]:
            print(el)
            if el["value"] != -1:
                val = el["value"]
                print(val)
                if flag:
                    el["flag"]=True
                    
                return val

    return -1

def returnChoice(el,question):

    if isChoice(el["item"]):
            if el["item"] != -1:
                q=el["item"].split(" ### ")
                if q[1] == question:
                    if el["value"] != -1:
                        return el["value"]
                        
    return -1

def covertStrToQueries(arr):
    arrOfQ=[]
    i=-1
    for element in arr:
        i+=1
        print("--------------------")
        print("itiration number :"+str(i))
        query=""
        question=""
        answer=""
        print("arr before Question: ")
        print(arr)
        print("item : "+element["item"])
        if isQuestion(element["item"]) and element["flag"] == False:
            if element["value"] != -1:
                ttr = element["item"]
                tt = ttr.split("$$")
                query+=tt[1]+","+element["value"]+","
                question=tt[0]
                element["flag"]=True

            print("question is :"+question)
            print("the answer is :")
            print("arr before answer: ")
            print(arr)
            if retAnswer(arr,question,False) != -1:
                answer=str(retAnswer(arr,question))
                query+=answer+","
                print(answer)
                
            
            # print(arr)

            print("the choicess is :")
            print("arr before choicess: ")
            print(arr)
            for el in arr:
                print(returnChoice(el,question))
                if returnChoice(el,question) != -1 and el["flag"]== False:
                    choice=str(returnChoice(el,question))
                    query+=choice+","
                    print(choice)
                    el["flag"]=True
        if query != "":
            arrOfQ.append(query)
            

    print("print the array :")
    print(arr)
    print("print the query :")
    print(arrOfQ)
    return arrOfQ

@login_required(login_url='/user/login/')
def addquiz(request):
    # request.POST["name"]
    name= ""
    time= ""
    passScore= ""
    dif= ""
    public= ""
    quiz=""
    queries=""
    requierd=["name","time","passScore","difficulty"]
    missing=False
    if not request.POST:
        return  render(request,'quiz/newquiz.html' , {}) 
    else:
        print("POST")
        for item in requierd:
            if item not in requierd:
                missing=True
        if not missing:
            obj=request.POST
            name = obj["name"]
            time = obj["time"]
            passScore = obj["passScore"]
            dif = obj["difficulty"]
        else : 
            HttpResponse("erorr in post data")
        arr =convertToArr(obj)
        print(arr)
        queries=covertStrToQueries(arr)
        print("name :"+name)
        print("time :"+time)
        print("passScore :"+passScore)
        print("dif :"+dif)
        NoQ=len(queries)
        if "ispublic" in obj:
            public = obj["ispublic"]
            print("public :"+public)
            quiz = Quiz(
                name=name,
                number_of_question= NoQ,
                time=time,
                score_to_pass=passScore,
                difficulty= dif,
                created_by= request.user,
                quiz_type= False,
            )
        else:
            quiz = Quiz(
                name=name,
                number_of_question= NoQ,
                time=time,
                score_to_pass=passScore,
                difficulty= dif,
                created_by= request.user,
                quiz_type= True,
            )
        quiz.save()

    #Answer, Question
    #['TorF,1+1=2,true,', 'MCQ,1+2,3,2,4,5,']
    for item in queries:
        el=item.split(",")
        el.pop(-1)
        t=el[0]
        q=el[1]
        
        question = addques(q,quiz,t)
        if question == -1:
            HttpResponse("something went wrong in adding Question")
        else:
            print (el[1]+" question is add to the database")

        answer_text=el[2]
        answer = addAns(answer_text,True,question,t)
        if answer == -1:
            HttpResponse("Something went wrong in adding Answer or Choice")
        
        for ch in el[3:]:
            answer = addAns(ch,False,question,t)
            if answer == -1:
                HttpResponse("Something went wrong in adding Answer or Choice")


    # print("quiz_ id :"+str(quiz.pk))
    print("done :)")
    messages.add_message(request,messages.SUCCESS,"Quiz has been added ")
    return  redirect('/myquizes' )
    

def addques(text,quiz,t):
    type=""
    if t == "MCQ":
        type="multiple"
    else:
        type="True or False"
    question = Question(
        text=text,
        quiz=quiz,
        type=type,
    )
    try:
        question.save()
        return question
    except Exception:
        return -1

def addAns(text,correct,question,t="noo"):
    new=False
    flag=False
    if t == "noo":
        1+1
    elif t == "MCQ":
        type="multiple"
    else:
        flag=True
        type="True or False"
        text=text.capitalize()
        if text == "True":
            new=False
        elif text == "False":
            new = True
            
    answer = Answer(
        text = text,
        correct = correct,
        question = question,
    )
    answer2 = Answer(
        text = new,
        correct = False,
        question = question,
    )
    try:
        answer.save()
        if flag:
            answer2.save()
        return answer
    except Exception:
        return -1

def addquestion(request):
     
    return  render(request,'teachers/addQuestion.html' , {}) 

def addAnswers(request):
    
    return  render(request,'teachers/addAnswers.html' , {}) 


