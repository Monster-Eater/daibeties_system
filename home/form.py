from django import forms
from django.forms import ModelForm
from .models import Reports


class resultForm(ModelForm):
    class Meta:
        model=Reports
        fields= "__all__"