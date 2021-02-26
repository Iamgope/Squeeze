from os import name
from django.db import models

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Question(models.Model):
    question = models.CharField(max_length=2000)
    opt1 = models.CharField(max_length=200)
    opt2 = models.CharField(max_length=200)
    opt3 = models.CharField(max_length=200)
    opt4 = models.CharField(max_length=200)
    correct = models.CharField(max_length=200)

    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='questions')
    

    def __str__(self):
        return f"Question {self.pk}"



    