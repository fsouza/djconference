#coding:utf-8
from core.models import Conference
from django import forms

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
