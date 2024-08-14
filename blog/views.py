from django.shortcuts import render
from django.views.generic import ListView
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

    def get_queryset(self):
        """Возвращает список объектов QUERYSET по нижеуказанным условиям, увеличивает
        счетчик просмотров, а так же сортирует по дате добавления"""
        queryset = super().get_queryset().order_by('posted_date',)
        for blog in queryset:
            blog.count_view += 1
            blog.save()  # Сохраняем изменения в БД
        return queryset
