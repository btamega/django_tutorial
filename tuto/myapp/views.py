from django.shortcuts import render
from django.http import HttpResponse

def home(request) :
    return HttpResponse('<h1>Hello world</h1>')
def about(request) :
    return HttpResponse('<h1>Vous êtes sur la page d\'à propos</h1>')
def contact(request) :
    return HttpResponse('<h1>Vous êtes sur la page de contact</h1>')
