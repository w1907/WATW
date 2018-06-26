from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import PersonalizarUserCreationForm

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


def registro_foro(request):
	template_name='registrar/registro.html'
	if request.method == 'POST':
		data = PersonalizarUserCreationForm(request.POST)
		if data.is_valid():
			data.save()
			messages.success(request, "Cuenta creada correctamente")
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			login(request, user)
			return HttpResponseRedirect(reverse('core.index'))
	else:
		data = PersonalizarUserCreationForm()
	return render(request, template_name, {'form': data})