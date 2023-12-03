from django.shortcuts import render
from .models import *


def slider(request):
    sliders = Slider.objects.filter(status=True)
    context = {
        'my_sliders': sliders
    }
    return render(request, 'index.html', context)
