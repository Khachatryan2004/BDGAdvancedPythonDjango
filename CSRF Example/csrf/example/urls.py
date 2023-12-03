from django.urls import path
from .views import index, add_message

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_message, name='add_message'),
]