from django.http import Http404
from django.shortcuts import get_object_or_404, render
from foro.models import Tema
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    data = {}
    object_list = Tema.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_page)

    template_name = 'foro/topic_list.html'
    return render(request, template_name, data)

def detail(request, topic_id):
    data = {}

    data['topic'] = get_object_or_404(Tema, pk=topic_id)

    template_name = 'foro/topic_detail.html'
    return render(request, template_name, data)

def news(request, topic_id):
    data = {}
    
    data['topic'] = get_object_or_404(Tema, pk=topic_id)
    object_list = Tema.objects.get(pk=topic_id).get_news.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_page)

    template_name = 'foro/topic_news.html'
    return render(request, template_name, data)