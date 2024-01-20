from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):

    def clean_price(self):
        value = self.cleaned_data['price']
        if value < 0:
            raise ValidationError("Not valid")
        return value


    class Meta:
        model = Product
        fields = ['name','description', 'price', 'category', 'stock']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User  #nesozdaemmodeltakkakonapodefoltu
        fields = ['username','password1','password2']