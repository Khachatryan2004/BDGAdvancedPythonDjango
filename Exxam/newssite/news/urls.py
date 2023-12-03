from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='news'),
    path('<slug:slug>/', AllNews.as_view(), name='news_list'),
    path('news_list/<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
]
