from tkinter.messagebox import RETRY
from django.shortcuts import render
from django.template import context

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About',
        'content': 'О нас',
        'text': 'О том, почему наш магазин самый классный..'
    }
    return render(request, 'main/about.html', context)