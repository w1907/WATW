from django.shortcuts import render
from foro.models import Tema

def index(request):
    data = {}

    data['topics'] = Tema.objects.all().order_by('-id')[:3]

    template_name = 'core/index.html'
    return render(request, template_name, data)
