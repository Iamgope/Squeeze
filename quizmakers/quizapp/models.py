from os import name, truncate
from django.db import models

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    code=models.CharField(max_length=10,default="12345678")

    def __str__(self) -> str:
        return self.name

class Question(models.Model):
    CORRECT_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]
    question = models.CharField(max_length=2000)
    opt1 = models.CharField(max_length=500)
    opt2 = models.CharField(max_length=500)
    opt3 = models.CharField(max_length=500)
    opt4 = models.CharField(max_length=500)
    correct = models.CharField(
        max_length=1,
        choices=CORRECT_CHOICES,
    )

    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='questions',blank=True)
    

    def __str__(self):
        return f"Question {self.pk}"



    