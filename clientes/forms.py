from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','last_name','age','rfid','deficiency_type','photo']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'age': 'Idade',
            'rfid': 'Identificador',
            'deficiency_type' : 'Deficiência',
            'photo': 'Foto',

        }

