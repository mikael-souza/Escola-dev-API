from django.db import models
from django.core.validators import MinLengthValidator


class Estudante(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11, unique=True) # unique ele irá verificar se existe um CPF igual àquele no banco de dados. Se existir, não será permitida a criação. Caso não exista, será permitido.
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome
        

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A','Avançando'),
    )
    codigo = models.CharField(max_length = 10, unique = True, validators=[MinLengthValidator(3)]) # Importamos esse ultimo parametro pois o django não possui um min como default   
    descricao = models.CharField(max_length = 100, blank = False)
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.codigo
    
class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N','Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete = models.CASCADE) # puxando modelos ja existentes com o Foreignkey e aplicando o on_delete, caso o estudante seja excluido, tudo relacionando a ele também será.
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    periodo = models.CharField(max_length = 1, choices = PERIODO, blank = False, null = False, default = 'M')