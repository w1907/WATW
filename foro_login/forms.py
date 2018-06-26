from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class PersonalizarUserCreationForm(forms.Form):
	username = forms.EmailField(label="Ingresa tu email")
	password = forms.CharField(label="Ingresa tu contraseña", widget=forms.PasswordInput)
	password_confirmar = forms.CharField(label="Confirma tu contraseña", widget=forms.PasswordInput)

	def validar_username(self):
		username = self.cleaned_data['username'].lower()
		existe = User.objects.filter(username=username)
		if existe.count():
			raise ValidationError("Correo electronico ya registrado")
		return username

	def validar_password_confirmar(self):
		password = self.cleaned_data.get('password')
		password_confirmar = self.cleaned_data.get('password_confirmar')
		if password and password_confirmar and password != password_confirmar:
			raise ValidationError("No coinciden las contraseñas")
		return password_confirmar

	def save(self, commit=True):
		usuario = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
		return usuario