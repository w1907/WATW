from django.urls import path
from . import views

urlpatterns=[
	path('login', views.login_foro, name="login_foro"),
	path('logout', views.logout_foro, name="logout_foro")
]