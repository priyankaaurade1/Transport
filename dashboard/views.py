from django.shortcuts import render,redirect
from django.http import HttpResponse

def index(request):

    return render(request, 'index.html')

def user_profile(request):
    return render(request, 'users-profile.html')

def pages_error_404(request):
    return render(request, 'pages-error-404.html')

def pages_contact(request):
    return render(request, 'pages-contact.html')

def pages_faq(request):
    return render(request, 'pages-faq.html')