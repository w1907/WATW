from django.urls import path
from . import views

urlpatterns = [
    path('topic', views.index, name="topic.index")
]