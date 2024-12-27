from django.shortcuts import render
from .models import Dishes
from django.views.generic import ListView



class DishesListView(ListView):
    model = Dishes
    template_name = "MainMenu.html"
    context_object_name = "dishes"



# Create your views here.
