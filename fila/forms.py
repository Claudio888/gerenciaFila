from django.forms import ModelForm
from django import forms

class FilaForm(forms.Form):
    nrfid = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(FilaForm, self).__init__(*args, **kwargs)
        self.fields['nrfid'].widget.attrs.update({'autofocus': ''})