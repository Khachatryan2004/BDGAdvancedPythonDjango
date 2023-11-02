from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home),
    path('my/<str:user_id>', user_request),
    path('cars/', show_carsell_list)
]
