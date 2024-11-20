from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return HttpResponse('hey i am a django server')
    peoples = [
        {'name': 'Tejas', 'age':21},
        {'name': 'virat', 'age':16},
        {'name': 'govind', 'age':15},
        {'name': 'john', 'age':25},
        {'name': 'deva', 'age':24},
    ]

    return render(request, 'index.html', context = {'page': 'Django 2024 tutorial', 'peoples':peoples})

def about(request):
    context = {'page': 'About'}
    return render(request, 'about.html', context)

def contact(request):
    context = {'page': 'Contact'}
    return render(request, 'contact.html', context)
