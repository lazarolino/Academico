from django.db import models

# Modelo predefinido para auxiliar no desenvolvimento

# class Livro(models.Model):
#     nome = models.CharField(max_length=100, verbose_name="Nome do livro")
#     autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor do livro")
#     editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name="Editora do livro")
#     genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Gênero do livro")
#     preco = models.IntegerField(verbose_name="Preço do livro")
#     data_plub = models.DateField(verbose_name="Data de publicação do livro")
#     status = models.BooleanField(verbose_name="Status do livro")
#     cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF do leitor")
    
#     def __str__(self):
#         return f'{self.nome}, {self.autor}'
    
#     class Meta:
#         verbose_name = "Livro"
#         verbose_name_plural = "Livros"

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Cidade")
    uf = models.CharField(max_length=2, verbose_name="Estado (UF)")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Profissão")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome completo")
    nome_pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    nome_mae = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.CharField(max_length=100, verbose_name="E-mail")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Profissão")

    def __str__(self):
        return f"{self.nome}, {self.cpf}"

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da instituição")
    site = models.CharField(max_length=100, verbose_name="Site")
    telefone = models.CharField(max_length=100, verbose_name="Telefone")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição de ensino"
        verbose_name_plural = "Instituições de ensino"


class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área do conhecimento")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do saber"
        verbose_name_plural = "Áreas do saber"


class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Curso")
    carga_horaria_total = models.FloatField(verbose_name="Carga horária total (h)")
    duracao_meses = models.IntegerField(verbose_name="Duração (meses)")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do conhecimento")
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de ensino")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Turma")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do conhecimento")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"


class Matricula(models.Model):
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    data_inicio = models.DateField(verbose_name="Data de início")
    data_previsao_termino = models.DateField(verbose_name="Previsão de término")
    # Alteraçao para fazer o matrícula e alunos
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

    def __str__(self):
        return f'{self.instituicao_ensino}'

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"


class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de avaliação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de avaliação"
        verbose_name_plural = "Tipos de avaliação"


class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    avaliacao_tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE, verbose_name="Tipo")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Aluno")
    numero_faltas = models.IntegerField(verbose_name="Número de faltas")

    def __str__(self):
        return f"{self.pessoa} - {self.disciplina}"

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"


class Turno(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Turno")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"


class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Aluno")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"


class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    carga_horaria = models.FloatField(verbose_name="Carga horária (h)")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    periodo = models.IntegerField(verbose_name="Período")

    def __str__(self):
        return f"{self.curso} - {self.disciplina}"

    class Meta:
        verbose_name = "Curso e Disciplina"
        verbose_name_plural = "Cursos e Disciplinas"

