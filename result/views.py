from django.shortcuts import render , HttpResponse , redirect
from django.http import JsonResponse
from django.views.generic import ListView
from question.models import Answer, Question
from result.models import Result

# Create your views here.



#class QuisListView(ListView):
#    model=Result
#    template_name='quiz/results.html'


#shows results
def results_view(request,id):
 
    print(id+"id")
    result=Result.objects.all().filter(quiz=id)

    print(result)

    return render(request , 'quizresult.html' ,
    {   
    "results" : result
    } )


