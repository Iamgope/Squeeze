from django.shortcuts import render
from .models import Question,Quiz
from django.utils import timezone


def landingPage(request):
    return render(request, 'landing.html', {})

def quizPage(request):
    quizz =  Quiz.objects.all

    return render(request,'give_quiz.html',{'quiz':quizz})

def addQuiz(request):
    if request.method == 'POST':
        quiz = Quiz()
        quiz.name = request.POST.get('quiz_name')
        quiz.save()
        quiz = Quiz.objects.all().last()
        return render(request, 'create_question.html', {'quiz': quiz })
    else:
        return render(request, 'create_quiz.html')