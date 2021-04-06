from django import forms


class GeneratorForm(forms.Form):
    textarea = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"placeholder": "Enter Text Here. Enter ____ (4 underscores) for the word you want to be predicted. E.g. I am a ____ person.",
               "class": "form-control-lg"}))

    def __init__(self, *args, **kwargs):
        super(GeneratorForm, self).__init__(*args, **kwargs)
        self.fields['textarea'].label = ""
