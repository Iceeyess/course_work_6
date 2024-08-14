from django.urls import path
from .apps import BlogConfig
from blog import views


app_name = BlogConfig.name

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
]