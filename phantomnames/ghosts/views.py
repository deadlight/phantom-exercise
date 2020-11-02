from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin
from .models import Ghost

def ghost_list(request):
    context = {
        'ghosts': Ghost.objects.all()
    }
    return render(request, 'ghosts/list.html', context)




def name_form(request):
    pass


def select_ghost(request):
    pass
