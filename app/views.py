from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from .forms import PessoaForm

# Página inicial
class IndexView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'index.html', {'pessoas': pessoas})

    def post(self, request):
        pass

# Novas views
class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})

class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})

class InstituicaoEnsinoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituicaoensino.html', {'instituicoes': instituicoes})

class AreaSaberView(View):
    def get(self, request, *args, **kwargs):
        areas = AreaSaber.objects.all()
        return render(request, 'areasaber.html', {'areas': areas})

class CursoView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})

class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})

class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})

class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas': matriculas})

class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes': avaliacoes})

class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})

class TurnosView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turno.objects.all()
        return render(request, 'turnos.html', {'turnos': turnos})

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencias': ocorrencias})

class CursoDisciplinaView(View):
    def get(self, request, *args, **kwargs):
        cursos_disciplinas = CursoDisciplina.objects.all()
        return render(request, 'cursodisciplina.html', {'cursos_disciplinas': cursos_disciplinas})

class AvaliacaoTipoView(View):
    def get(self, request, *args, **kwargs):
        tipos = AvaliacaoTipo.objects.all()
        return render(request, 'avaliacaotipo.html', {'tipos': tipos})

# Pessoa: excluir
class DeletePessoaView(View):
    def get(self, request, id, *args, **kwargs):
        pessoa = Pessoa.objects.get(id=id)
        pessoa.delete()
        messages.success(request, 'Pessoa excluída com sucesso!')
        return redirect('pessoas')

# Pessoa: editar
class EditarPessoaView(View):
    template_name = 'editar_pessoa.html'

    def get(self, request, id, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, id=id)
        form = PessoaForm(instance=pessoa)
        return render(request, self.template_name, {'pessoa': pessoa, 'form': form})

    def post(self, request, id, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, id=id)
        form = PessoaForm(request.POST, instance=pessoa)

        if form.is_valid():
            form.save()
            messages.success(request, 'As edições foram salvas com sucesso.')
            return redirect('editar', id=id)
        else:
            messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
            return render(request, self.template_name, {'pessoa': pessoa, 'form': form})
