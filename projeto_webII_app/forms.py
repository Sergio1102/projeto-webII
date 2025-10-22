from django import forms
from .models import Evento, Local, Palestrante, CategoriaEvento

class FormularioEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'data_hora': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'palestrantes': forms.CheckboxSelectMultiple,
        }

class FormularioLocal(forms.ModelForm):
    class Meta:
        model = Local
        fields = '__all__'

class FormularioPalestrante(forms.ModelForm):
    class Meta:
        model = Palestrante
        fields = '__all__'

class FormularioCatEvento(forms.ModelForm):
    class Meta:
        model = CategoriaEvento
        fields = '__all__'