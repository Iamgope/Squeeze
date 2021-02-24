from django.shortcuts import render

# Create your views here.
def landingPage(request):
    return render(request, 'template/landing.html', {})
def signinPage(request):
    return render(request, 'template/signin.html', {})