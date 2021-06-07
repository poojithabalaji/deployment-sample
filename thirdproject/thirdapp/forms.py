from django import forms
from django.forms import ModelForm
from thirdapp.models import Users

class formname(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name','last_name','email']
