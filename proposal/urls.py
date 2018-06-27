from django.urls import path
from . import views

urlpatterns = [
    path('topic/<int:topic_id>/proposal/', views.index, name="proposal.list"),
    path('topic/<int:topic_id>/proposal/<int:proposal_id>/', views.detail, name="proposal.detail")
]