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
def results_view(request,pk):
    
    try:
        result=Result.objects.get(pk=pk)
        #result=Result.objects.get(id=1)
    except Exception:
        return HttpResponse("error")
    
    return render(request , 'quizresult.html' ,
    {   
    "results" : result
    } )


