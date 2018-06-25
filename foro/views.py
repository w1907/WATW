from django.shortcuts import render

def index(request):
    data = {}
    template_name = 'foro/topic.html'
    return render(request, template_name, data)