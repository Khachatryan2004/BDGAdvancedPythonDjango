from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    return HttpResponse('<h1>You Are In Home Page</h1>')


def user_request(request, user_id):
    return HttpResponse(f'<h1>Your request is {user_id}</h1>')


def show_carsell_list(request):
    cars = CarSell.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'cars.html', context)
