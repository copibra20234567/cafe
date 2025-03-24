from cafeApp.views import MainListView, MenuListView, CartView, RegisterView, LoginViewCustom, AddToCartView, CartUpdateView, CartDeleteView, OrderCreateView, OrderListView
from django.urls import path, include
from django.contrib.auth.views import LogoutView
app_name = 'cafeApp'
urlpatterns = [
    path('', MainListView.as_view(), name='main-list'),
    path('dishes/', MenuListView.as_view(), name='dishes-list'),
    path('add_to_cart/<int:dish_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name ='shopping-cart'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginViewCustom.as_view(next_page='cafeApp:main-list'), name='login'),
    path('logout/', LogoutView.as_view(next_page='cafeApp:login'), name='logout'),
    path('edit_cart/<int:pk>/', CartUpdateView.as_view(), name='edit-cart'),
    path('cart/delete/<int:pk>/', CartDeleteView.as_view(), name='delete-cart-item'),
    path('order/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/', OrderListView.as_view(), name='order-list')

]
