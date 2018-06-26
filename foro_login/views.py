from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

def login_foro(request):
	data = {}
	template_name = 'login/login.html'
	logout(request)
	username = password = ''

	if request.POST:
		username = request.POST['inputEmail']
		password = request.POST['inputPassword']

		user = authenticate(username=username,password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('core.index'))
			else:
				messages.warning(request, "Correo o contraseña invalidos")
		else:
			messages.warning(request, "Correo o contraseña invalidos")
	return render(request, template_name, data)


def logout_foro(request):
	logout(request)
	return HttpResponseRedirect(reverse('core.index'))