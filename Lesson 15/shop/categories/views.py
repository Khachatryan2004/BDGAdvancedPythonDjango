from django.shortcuts import render

from categories.models import Category


# Create your views here.

def home(request):
    categories = Category.objects.filter(status=True)
    context = {
        'categories': categories
    }
    return render(request, 'categories/index.html', context)
