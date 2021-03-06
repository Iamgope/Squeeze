from django import forms

from .models import Quiz,Question
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class PostQuiz(forms.ModelForm):

    class Meta:
        model=Question
        fields =('question','opt1','opt2','opt3','opt4','correct')

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']