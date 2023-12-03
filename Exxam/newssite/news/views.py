from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_list = Category.objects.all()

        paginator = Paginator(categories_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            categories = paginator.page(page)
        except PageNotAnInteger:
            categories = paginator.page(1)
        except EmptyPage:
            categories = paginator.page(paginator.num_pages)

        context['categories'] = categories
        return context


class AllNews(DetailView):
    model = Category
    template_name = 'next.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new = self.get_object()
        context['news_all'] = News.objects.filter(news=new)
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'about.html'
    context_object_name = 'news'
