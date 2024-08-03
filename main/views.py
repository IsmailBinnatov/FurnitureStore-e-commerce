from unicodedata import category
from django.shortcuts import render

from goods.models import Category


# Create your views here.
def index(request):
    category = Category.objects.all()

    context = {
        'title': 'Home',
        'content': 'Магазин мебели HOME',
        'categories': category,
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About',
        'content': 'О нас',
        'text': 'О том, почему наш магазин самый классный..'
    }
    return render(request, 'main/about.html', context)
