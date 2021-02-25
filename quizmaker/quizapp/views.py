from django.shortcuts import render

# create a dictionary 
context = { 
    "quiz" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
} 
    # return response 
    # return render(request, "geeks.html", context) 

# Create your views here.
def landingPage(request):
    return render(request, 'landing.html', {})
def signinPage(request):
    return render(request, 'give_quiz.html', context)