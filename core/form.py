from .models import *
from django.forms import ModelForm


class postosForm(ModelForm):
    class Meta:
        model = postos
        fields = ["pos_nome", "pos_cep","pos_rua","pos_bairro","pos_numero","pos_logradouro","pos_telefone"]

class vacinasForm(ModelForm):
    class Meta:
        model = vacinas
        fields = ["vac_tipo_vacina", "vac_lote", "vac_fabricante","vac_descricao","vac_quantidade","vac_disponibilidade","vac_contraindicacao","vac_reacoes","vac_data_fabricacao","vac_data_validade","vac_data_recebimento"]  