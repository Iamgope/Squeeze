from django.urls import path
from . import views

app_name = 'quizapp'

urlpatterns = [
    path('', views.landingPage, name='landing'),
    path('give_quiz/', views.quizPage, name='quiz'),
    path('quiz/<int:pk>/', views.quiz_detail, name='quiz_detail'),
    path('create_quiz/', views.addQuiz, name='create'),
    path('add_question/<int:pk>',views.addQuestion, name='add_question'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),
    #path('create_question/', views.addQuiz, name='create'),
]