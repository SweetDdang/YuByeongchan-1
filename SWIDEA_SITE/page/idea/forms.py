from django import forms
from .models import Idea, Dev_tool

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = '__all__'

class DevForm(forms.ModelForm):
    class Meta:
        model = Dev_tool
        fields = '__all__'