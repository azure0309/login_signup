from django.shortcuts import render
from django.http import HttpResponse
from . import views

# Create your views here.
def index(response):
    return HttpResponse('I Love You 3000!!!')
