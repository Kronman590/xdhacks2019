<<<<<<< HEAD
from django.shortcuts import render
from django.template import Template, Context 

def index(request):
    return render(request, 'registration/login.html')

# Create your views here.
=======
from django.http import HttpResponse

def index(request):
    return HttpResponse("Whats goood my doods")

# Create your views here.
>>>>>>> 22d5165b103ce3c6ccfa5eba9a577a7d7bdfb205
