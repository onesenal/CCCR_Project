from django.shortcuts import render
from .models import world

# 메인 페이지
def index(request):
    worlds = world.objects
    return render(request, 'pybo/main_page.html', {'worlds': worlds} )

def detail(request, world_id):
    wi = world.objects.get(id=world_id)
    pi = 'hello'
    context = {'wi': wi, 'pi' : pi}
    return render(request, 'pybo/reserv_form.html', context)

def reservation(request, world_id):
    worlds = world.objects
    context = {'worlds': worlds}
    return render(request, 'pybo/main_page.html', context)