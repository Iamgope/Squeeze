from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=2000)
    opt1 = models.CharField(max_length=200)
    opt2 = models.CharField(max_length=200)
    opt3 = models.CharField(max_length=200)
    opt4 = models.CharField(max_length=200)
    correct = models.CharField(max_length=200)

    def __str__(self):
        return f"Question {self.pk}"

class Quizzes(models.Model):
    name = models.CharField(max_length=200)
    questions = models.ManyToManyField(Questions)

    def __str__(self):
        return self.name
     
