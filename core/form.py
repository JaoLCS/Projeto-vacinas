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
        self.fields['vac_disponibilidade'].widget.attrs.update({'class': 'form-select'}) 
    class Meta:
        model = vacinas
        fields = ["vac_tipo_vacina", "vac_lote", "vac_fabricante","vac_descricao","vac_quantidade","vac_disponibilidade","vac_contraindicacao","vac_reacoes","vac_data_fabricacao","vac_data_validade","vac_data_recebimento", "vac_posto"]  