from django import forms
from app.models import *
class MoviesForm(forms.ModelForm):
    class Meta():
        model=Movies
        fields='__all__'