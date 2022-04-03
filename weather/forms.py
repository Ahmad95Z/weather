from dataclasses import fields
from pyexpat import model
from .models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta():
        model = City
        fields = ['name']
        vidgets = {'name': TextInput(attrs={
            'class':'form-control','name':'city','aria-label':'Sizing example input',
            ' aria-describedby':'inputGr','id':'city','placeholder':'Укажите город'})}