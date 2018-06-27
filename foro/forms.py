from django import forms
from .models import Tema

class AddTopicForm(forms.ModelForm):

	class Meta:
		model = Tema
		fields = [
			'titulo',
			'contenido',
			'imagen',
		]
		labels = {
			'titulo': 'Ingresa titulo',
			'contenido': 'Ingresa contenido',
			'imagen': 'Ingresa imagen',
		}
		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'contenido': forms.Textarea(attrs={'class':'form-control'}),
			'imagen': forms.FileInput(attrs={'class':'form-control'}),
		}