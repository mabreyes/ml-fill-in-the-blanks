from django import forms

class GeneratorForm(forms.Form):
    textarea = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(GeneratorForm, self).__init__(*args, **kwargs)
        self.fields['textarea'].label = "Enter Text Here"