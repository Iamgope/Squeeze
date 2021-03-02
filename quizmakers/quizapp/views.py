from django.shortcuts import render,get_object_or_404
from .models import Question,Quiz
from django.utils import timezone
from .forms import PostQuiz
from django.shortcuts import redirect
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
# main landing Page
def landingPage(request):
    return render(request, 'landing.html', {})




# quizPage and Details
def quizPage(request):
    quiz =  Quiz.objects.all
    return render(request,'give_quiz.html',{'quiz':quiz})

def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    return render(request, 'quiz_detail.html', {'quiz': quiz})




#creating quiz
def addQuiz(request):
    

    if request.method == 'POST':
        quiz = Quiz()
       
        quiz.name = request.POST.get('quiz_name')
        quiz.save()
        quiz = Quiz.objects.all().last()
        k=quiz.pk
        s='/add_question/'+str(k)+''
        
        return redirect(s)
    else:
        return render(request, 'create_quiz.html')


def addQuestion(request,pk):
    quiz = get_object_or_404(Quiz, pk=pk)
   
    if request.method =='POST':
        form = PostQuiz(request.POST)
        if form.is_valid():
            quest =form.save(commit=False)
            #quest.question= request.POST.get('question')
            quest.quiz=quiz
            
            quest.save()
            
       # quest=Question.objects.all().last()
            return render(request,'create_question.html',{'form':form})
    else:
        form = PostQuiz()
        return render(request,'create_question.html',{'form':form})








