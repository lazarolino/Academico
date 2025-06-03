from django.contrib import admin
from .models import *

# Registro simples dos modelos
admin.site.register(Cidade)
admin.site.register(Turma)
admin.site.register(Matricula)
admin.site.register(AvaliacaoTipo)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turno)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)

# Inlines e Admins personalizados

# i) Pessoa e ocupação
class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

admin.site.register(Ocupacao, OcupacaoAdmin)

# ii) Instituição e cursos
class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)

# iii) Área do saber e cursos
class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInline]  # Reaproveita o inline já definido

admin.site.register(AreaSaber, AreaSaberAdmin)

# iv) Cursos e disciplinas
class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]

admin.site.register(Curso, CursoAdmin)

# v) Disciplinas e avaliações
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

admin.site.register(Disciplina, DisciplinaAdmin)

# vi) Matrícula e alunos
class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

# Atualiza PessoaAdmin com frequência e matrícula
class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline, FrequenciaInline]

admin.site.register(Pessoa, PessoaAdmin)
