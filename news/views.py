from django.shortcuts import render, get_object_or_404
from foro.models import *

def detail(request, topic_id, new_id):
    data = {}

    data['new'] = get_object_or_404(Noticia, pk=new_id)
    data['topic'] = get_object_or_404(Tema, pk=topic_id)

    template_name = 'news/news_detail.html'
    return render(request, template_name, data)