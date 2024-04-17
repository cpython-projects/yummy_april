from django.shortcuts import render
from django.http import HttpResponse
from .models import DishCategory, Dish, Gallery


# Create your views here.
def index(request):
    categories = DishCategory.objects.filter(is_visible=True)
    gallery = Gallery.objects.all()

    context = {
        'title_menu': 'Check Our <span>Yummy Menu</span>',
        'title_gallery': 'Check <span>Our Gallery</span>',
        'categories': categories,
        'gallery': gallery,
    }

    return render(request, 'main.html', context=context)


def manager(request):
    ...