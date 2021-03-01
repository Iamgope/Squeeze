from django.shortcuts import render,get_object_or_404
from .models import Question,Quiz
from django.utils import timezone
from .forms import PostQuiz,PostQuestion
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
        return render(request, 'create_question.html', {'quiz': quiz })
    else:
        return render(request, 'create_quiz.html')


def add_new(request):
    if request.method == "POST":
        form = PostQuiz(request.POST)
        if form.is_valid():
            quiz = Quiz()
            quiz.name = request.POST.get('quiz_name')
            quiz.save()
            quiz = Quiz.objects.all().last()
        form= PostQuestion()
        if form.is_valid():
            post = form.save(commit=False)
           
            post.quiz=Quiz
            post.save()
        return render(request, 'create_question.html', {'form': form})
            
    else:
        form = PostQuiz()
        return render(request, 'create_quiz.html', {'form': form})

def add_question(request,name):
    form= PostQuestion()
    if form.is_valid():
            post = form.save(commit=False)
            
            post.save()
            return redirect('give_quiz.html')
            post.save()
            


class QuizCreateView(CreateView):
    model = Quiz
    fields = ('name', )
    template_name = 'create_quiz.html'

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        messages.success(self.request, 'The quiz was created with success! Go ahead and add some questions now.')
        return redirect('quiz_change', quiz.pk)

class QuizUpdateView(UpdateView):
    model = Quiz
    fields = ('name', 'subject', )
    context_object_name = 'quiz'
    template_name = 'quiz_change_form.html'

    def get_context_data(self, **kwargs):
        kwargs['questions'] = self.get_object().questions.annotate(answers_count=Count('answers'))
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        '''
        This method is an implicit object-level permission management
        This view will only match the ids of existing quizzes that belongs
        to the logged in user.
        '''
        return self.request.user.quizzes.all()

    def get_success_url(self):
        return reverse('quiz_change', kwargs={'pk': self.object.pk})