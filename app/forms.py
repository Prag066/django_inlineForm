from django import forms
from django.forms import formset_factory


class ArticalForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()

    