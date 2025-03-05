from django.shortcuts import render
from .models import Dishes, Cart
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy

class MainListView(ListView):
    model = Dishes
    template_name = "MainMenu.html"
    context_object_name = "Dishes"


class MenuListView(ListView):
    model = Dishes
    template_name = "DishesList.html"
    context_object_name = "All_dishes"



class CartView(ListView):
    model = Cart
    template_name = 'Cart.html'
    context_object_name = 'cart_items'



    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Cart.objects.filter(user=self.request.user)
        else:
            session_key = self.request.session.session_key
            return Cart.objects.filter(session_key=session_key)


class AddToCartView(View):
    def get(self, request, dish_id, *args, **kwargs):
        dish = get_object_or_404(Dishes, id=dish_id)
        dish_id = self.kwargs.get('dish_id')
        cart = request.session.get('cart', [])  # Отримуємо кошик з сесії
        cart.append(dish_id)  # Додаємо ID товару
        request.session['cart'] = cart  # Зберігаємо у сесії

        if request.user.is_authenticated:
            cart_item, created = Cart.objects.get_or_create(user=request.user, dish=dish)
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key

            cart_item, created = Cart.objects.get_or_create(session_key=session_key, dish=dish)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect(reverse_lazy('cafeApp:shopping-cart'))


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)  # Автоматично логінити після реєстрації
            return redirect('MainMenu.html')  # Перенаправлення на головну сторінку
        return render(request, 'register.html', {'form': form})


class auth_views(LoginView):
    template_name = 'login.html'  # Вказуємо власний шаблон
    redirect_authenticated_user = True  # Якщо користувач вже увійшов, перенаправити
# Create your views here.
