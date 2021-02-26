from django.shortcuts import render
from .models import Question,Quiz
from django.utils import timezone
# create a dictionary 

    # return response 
    # return render(request, "geeks.html", context) 

# Create your views here.
def landingPage(request):
    return render(request, 'landing.html', {})

def quizPage(request):
    quizz =  Quiz.objects.all

    return render(request,'give_quiz.html',{'quiz':quizz})
