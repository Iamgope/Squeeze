from django.urls import path
from . import views

app_name = 'quizapp'

urlpatterns = [
    path('', views.landingPage, name='landing'),
    path('give_quiz/', views.quizPage, name='quiz'),
    path('quiz/<int:pk>/', views.quiz_detail, name='quiz_detail'),
    path('create_quiz/', views.QuizCreateView, name='create'),
    path('quiz/new/', views.add_new, name='add_new'),
    path('quiz/new/<int:pk>/', views.QuizUpdateView.as_view(), name='quiz_change'),
]