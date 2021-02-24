from django.shortcuts import render

# Create your views here.
def landingPage(request):
    return render(request, 'landing.html', {})
def signinPage(request):
    return render(request, 'signin.html', {})