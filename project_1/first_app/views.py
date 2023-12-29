from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
    return HttpResponse("First_app/home")
def course(response):
    return HttpResponse("First_app/Courses section .")
def about(response):
    return HttpResponse("first_app/About section ")
