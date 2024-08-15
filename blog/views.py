from django.shortcuts import render
from django.views.generic import ListView, DetailView
from config.settings import TOPIC_TUPLE
from blog.models import Blog
from .apps import BlogConfig

topic_name = BlogConfig.name

# Create your views here.


class BlogListView(ListView):
    model = Blog
    paginate_by = 2
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.count_view += 1
        obj.save()
        return obj