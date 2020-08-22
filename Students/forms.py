from django import forms
from .models import JuniorRound

class junior_round_form(forms.ModelForm):
    class Meta:
        model = JuniorRound
        fields = ('full_name','fathers_name','address','class_name','school_name','mobile_number','email','image')
