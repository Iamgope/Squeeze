from django.shortcuts import render,get_object_or_404
from .models import Question,Quiz
from django.utils import timezone
from .forms import PostQuiz,CreateUserForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,UpdateView)
cool=False
# main landing Page
def registerPage(request):
    
    if request.user.is_authenticated:
        return redirect('quizapp:landing')
	
    else:    
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('/login/')
                

        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        
        return redirect('quizapp:landing')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                cool=True
                login(request, user)
                return redirect('quizapp:landing')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('quizapp:login')



def landingPage(request):
    if request.user.is_authenticated:
        return render(request, 'navout.html')
    else:
        return render(request,'navin.html')



 
# quizPage and Details
def quizPage(request):
    if request.method=='POST':
        code=request.POST.get('code')
        quiz =  Quiz.objects.filter(code=str(code))
        if quiz:
            return redirect('/quiz/'+str(quiz[0].pk)+'' )
           
        return render(request,'give_quiz.html',{'quiz':quiz})
    else:
        quiz =  Quiz.objects.all
        return render(request,'give_quiz.html',{'quiz':quiz})


@login_required(login_url='quizapp:login')

def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == 'POST':
        response = request.POST
        # print(response)
        cor = 0
        for i in response:
            i = i.split(' ')
            if i[0] == 'Question':
                ans = Question.objects.get(pk=int(i[1])).correct
                resp = response['Question '+i[1]]
                # print(resp, ans)
                if resp == ans:
                    cor += 1
        # print("No. of correct answers: ", cor, ".")
        return render(request, 'result.html', {'quiz': quiz, 'correct': cor})
        
    else:
        return render(request, 'quiz_detail.html', {'quiz': quiz})




#creating quiz
@login_required(login_url='quizapp:login')
def addQuiz(request):
    

    if request.method == 'POST':
        quiz = Quiz()
       
        quiz.name = request.POST.get('quiz_name')
        quiz.code=request.POST.get('code')
        quiz.save()
        quiz = Quiz.objects.all().last()
        k=quiz.pk
        s='/add_question/'+str(k)+''
        
        return redirect(s)
    else:
        return render(request, 'create_quiz.html')

@login_required(login_url='quizapp:login')
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
            return render(request,'update.html',{'PK':pk})
    else:
        form = PostQuiz()
        return render(request,'create_question.html',{'form':form})







