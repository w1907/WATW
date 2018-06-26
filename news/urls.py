from django.urls import path
from . import views as news

urlpatterns = [
    path('topic/<int:topic_id>/news/<int:new_id>/', news.detail, name="news.detail")
]