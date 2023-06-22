from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cepa, Tipo, InventoryItem


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class InventoryItemForm(forms.ModelForm):
	Cepa = forms.ModelChoiceField(queryset=Cepa.objects.all(), initial=0)
	Tipo = forms.ModelChoiceField(queryset=Tipo.objects.all(), initial=0)
	class Meta:
		model = InventoryItem
		fields = ['Nombre', 'Cepa', 'Tipo', 'Viña', 'Año', 'Cantidad']