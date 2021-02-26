from django.shortcuts import render,get_object_or_404
from .models import Question,Quiz
from django.utils import timezone


def landingPage(request):
    return render(request, 'landing.html', {})

def quizPage(request):
    quiz =  Quiz.objects.all
    return render(request,'give_quiz.html',{'quiz':quiz})

def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    return render(request, 'quiz_detail.html', {'quiz': quiz})

def addQuiz(request):
    if request.method == 'POST':
        quiz = Quiz()
        quiz.name = request.POST.get('quiz_name')
        quiz.save()
        quiz = Quiz.objects.all().last()
        return render(request, 'create_question.html', {'quiz': quiz })
    else:
        return render(request, 'create_quiz.html')