from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Vk


class VkForm(forms.ModelForm):
    vk = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Токен VK Admin'}))
    class Meta:
        model = Vk
        fields = ('vk',)