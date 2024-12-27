from cafeApp.views import DishesListView
from django.urls import path, include

urlpatterns = [
    path('', DishesListView.as_view(), name='dishes-list')
]
