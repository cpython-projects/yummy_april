from django.shortcuts import render, redirect
from django.contrib import messages
from .models import DishCategory, Dish, Gallery
from .forms import ReservationForm
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        gallery = Gallery.objects.all()
        form = ReservationForm()

        context['title_menu'] = 'Check Our <span>Yummy Menu</span>'
        context['title_gallery'] = 'Check <span>Our Gallery</span>'
        context['categories'] = categories
        context['gallery'] = gallery
        context['form'] = form

        return context

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше бронювання прийнято!')
            return redirect('main:index')


def manager(request):
    ...