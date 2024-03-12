from django import forms
from .models import Recipe, User


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = [
            'id'
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['id']
        # labels = {'name': 'Имя',
        #           'email': 'Почта'}

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'name']
