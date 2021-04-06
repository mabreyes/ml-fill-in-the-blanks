from django import forms

class GeneratorForm(forms.Form):
    textarea = forms.CharField(max_length=100)