from cafeApp.views import MainListView, MenuListView, CartView, RegisterView, auth_views, AddToCartView
from django.urls import path, include
app_name = 'cafeApp'
urlpatterns = [
    path('', MainListView.as_view(), name='main-list'),
    path('dishes/', MenuListView.as_view(), name='dishes-list'),
    path('add_to_cart/<int:dish_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name ='shopping-cart'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.as_view, name='login')
]
