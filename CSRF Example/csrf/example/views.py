from django.shortcuts import render, redirect
from .models import Message
from django.http import HttpResponse


def index(request):
    messages = Message.objects.all()
    context = {
        'messages': messages
    }
    return render(request, 'example/index.html', context)


def add_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(content=content)
            return redirect('index')
        else:
            return HttpResponse('Invalid content')
    else:
        return HttpResponse('Invalid request method')
