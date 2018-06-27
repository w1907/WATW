from django.shortcuts import render, get_object_or_404
from foro.models import Tema, PropuestaSolucion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request, topic_id):
    data = {}
    data['topic'] = get_object_or_404(Tema, id=topic_id)
    object_list = data['topic'].get_proposals.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_page)

    template_name = 'proposal/proposal_list.html'
    return render(request, template_name, data)

def detail(request, topic_id, proposal_id):
    data = {}
    data['proposal'] = get_object_or_404(PropuestaSolucion, id=proposal_id)
    data['topic'] = get_object_or_404(Tema, id=topic_id)
    
    template_name = 'proposal/proposal_detail.html'
    return render(request, template_name, data)
