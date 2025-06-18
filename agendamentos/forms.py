from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'data', 'hora', 'servicos']
        widgets = {
            'servicos': forms.CheckboxSelectMultiple(),
        }

    def clean_servicos(self):
        servicos = self.cleaned_data.get('servicos')
        if not servicos:
            raise forms.ValidationError('Escolha pelo menos um serviço.')
        return servicos
