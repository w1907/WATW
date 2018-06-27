from django.urls import path
from . import views
from news import views as news

urlpatterns = [
    path('topic', views.index, name="topic.index"),
    path('topic/<int:topic_id>/', views.detail, name="topic.detail"),
    path('topic/<int:topic_id>/news/', views.news, name="topic.news"),
    path('topic/add', views.add_topic, name="add_topic")
]