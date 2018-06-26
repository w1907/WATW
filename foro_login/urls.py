from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
	path('login', views.login_foro, name="login_foro"),
	path('logout', views.logout_foro, name="logout_foro"),
	path('register', views.registro_foro, name="registro_foro"),
]