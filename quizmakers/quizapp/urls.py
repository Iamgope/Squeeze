from django.urls import path
from . import views

app_name = 'quizapp'

urlpatterns = [
    path('', views.landingPage, name='landing'),
    path('give_quiz/', views.quizPage, name='quiz'),
    path('create_quiz/', views.addQuiz, name='create'),
]