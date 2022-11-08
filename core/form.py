from .models import *
from django.forms import ModelForm
from django import forms

class postosForm(ModelForm):
    class Meta:
        model = postos
        fields = ["pos_nome", "pos_cep","pos_rua","pos_bairro","pos_numero","pos_logradouro","pos_telefone"]

class vacinasForm(ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vac_posto'].widget.attrs.update({'class': 'form-select'}) 
        self.fields['vac_descricao'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['vac_disponibilidade'].widget.attrs.update({'class': 'form-select'}) 
        self.fields['vac_contraindicacao'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['vac_reacoes'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['vac_tipo_vacina'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['vac_lote'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['vac_quantidade'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['vac_fabricante'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['vac_data_fabricacao'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['vac_data_validade'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['vac_data_recebimento'].widget.attrs.update({'class': 'form-control'}) 

    class Meta:
        model = vacinas
        fields = '__all__'
        widgets = {
        'vac_dias': forms.CheckboxSelectMultiple(attrs= {'class' : 'form-check-input'}),
        }