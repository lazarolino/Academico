# Alterações feitas:
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Pessoa
#

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'pessoa',
            'ocupacao',
            'instituicaoensino',
            'areasaber',
            'curso',
            'turma',
            'disciplina',
            'matricula',
            'avaliacao',
            'frequencia',
            'turnos',
            'cidade',
            'ocorrencia',
            'cursodisciplina',
            'avaliacaotipo',
            Submit('submit', 'Salvar')
        )
