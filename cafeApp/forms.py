from django import forms
from django.contrib.auth.models import User
from .models import Cart, Order
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Підтвердження пароля", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean_password2(self):
        if self.cleaned_data["password"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("Паролі не співпадають")
        return self.cleaned_data["password2"]
class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['dish', 'quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["full_name", "address", "credit_card"]
        widgets = {
            "credit_card": forms.TextInput(attrs={"type": "password"}),  # Приховуємо кредитну карту
        }