from django import forms
from .models import *

class SketchForm(forms.ModelForm):
    class Meta:
        model = Sketch
        fields = ['name', 'image']