from django import forms

from .models import Quiz,Question


class PostQuiz(forms.ModelForm):

    class Meta:
        model=Quiz
        fields =('name',)


class PostQuestion(forms.ModelForm):

    class Meta:
        model=Question
        fields =('question','opt1','opt2','opt3','opt4','correct')

