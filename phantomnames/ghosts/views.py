from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Ghost

def ghost_list(request):
    context = {
        'ghosts': Ghost.objects.all()
    }
    return render(request, 'ghosts/list.html', context)


def name_form(request):
    context = {}
    return render(request, 'ghosts/form.html', context)


def select_ghost(request):
    response = None

    first_name = request.POST.get("first-name", None)
    last_name = request.POST.get("last-name", None)

    if first_name is None or last_name is None:
        response = redirect('/get-name')

    if response is None:
        ghost_options = Ghost.objects.filter(user=None).order_by("?")[:3]
        context = {
            'ghosts': ghost_options,
            'first_name': first_name,
            'last_name': last_name,
        }
        response = render(request, 'ghosts/select.html', context)

    return response


def confirm_ghost(request):
    response = None

    first_name = request.POST.get("first-name", None)
    last_name = request.POST.get("last-name", None)
    selected_ghost_id = request.POST.get("ghost", None)
    selected_ghost = Ghost.objects.get(id=selected_ghost_id)
    confirmed = request.POST.get("confirm", None)
    selected_ghost = Ghost.objects.get(id=selected_ghost_id)

    if first_name is None or last_name is None:
        response = redirect('/get-name')
    elif not selected_ghost:
        response = redirect('/select-ghost')

    if confirmed is not None:
        response = redirect('/')
        if confirmed == 'yes':
            try:
                existing_ghost = Ghost.objects.get(user=request.user)
            except ObjectDoesNotExist:
                existing_ghost = None
            if existing_ghost:
                existing_ghost.first_name = None
                existing_ghost.last_name = None
                existing_ghost.user = None
                existing_ghost.save()

            selected_ghost.first_name = first_name
            selected_ghost.last_name = last_name
            selected_ghost.user = request.user
            selected_ghost.save()

    if response is None:
        selected_name = first_name + ' "' + selected_ghost.name + '" ' + last_name
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'ghost': selected_ghost_id,
            'selected_name': selected_name,
        }
        response = render(request, 'ghosts/confirm.html', context)

    return response