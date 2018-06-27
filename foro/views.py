from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from foro.models import Tema
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AddTopicForm

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

def add_topic(request):
    template_name = 'foro/topic_add.html'
    if request.method == 'POST':
        form = AddTopicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('topic.index'))
    else:
        form = AddTopicForm()
    return render(request, template_name, {'form':form})

def edit_topic(request, topic_id):
    template_name = 'foro/topic_add.html'
    topic = Tema.objects.get(id=topic_id)
    if request.method == 'GET':
        form = AddTopicForm(instance=topic)
    else:
        form = AddTopicForm(request.POST, request.FILES, instance=topic)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('topic.index'))
    return render(request, template_name, {'form': form})

def delete_topic(request, topic_id):
    template_name = 'foro/topic_delete.html'
    topic = Tema.objects.get(id=topic_id)
    if request.method == 'GET':
        topic.delete()
        return HttpResponseRedirect(reverse('topic.index'))
    return render(request, template_name, {'form': topic})