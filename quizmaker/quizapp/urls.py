from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name='landing'),
    path('give_quiz/', views.signinPage, name='give_quiz'),
]