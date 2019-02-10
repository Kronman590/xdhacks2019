from django.shortcuts import render
from django.template import Template, Context 

def index(request):
    return render(request, 'registration/login.html')

# Create your views here.
