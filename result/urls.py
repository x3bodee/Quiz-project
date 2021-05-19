from django.urls import path
from quiz import views 
from django.conf.urls.static import static
from django.conf import settings
from .views import (

    results_view,
    
)

urlpatterns = [

    path('result/<id>' , results_view , name="results_view"),

    
]

