from django.db import models

# Create your models here.

class Questoes(models.Model):
    segmento_choices = (('F', 'Ensino Fundamental'),
                        ('M', 'Ensino Médio'))

    ano_choices = (('6', '6º Ano'),
                 ('7', '7º Ano'),
                 ('8', '8º Ano'),
                 ('9', '9º Ano'),
                 ('1', '1º Ano E.M.'),
                 ('2', '2º Ano E.M.'),
                 ('3', '3º Ano E.M.'))
    nivel_choices = (('Fa', 'Fácil'),
                    ('Me', 'Médio'),
                    ('De', 'Difícil'))

    nome = models.CharField(max_length=100)
    segmento = models.CharField(max_length=2, choices=segmento_choices, default="F")
    ano = models.CharField(max_length=2, choices=ano_choices, default="6")
    nivel = models.CharField(max_length=2, choices=nivel_choices, default="Fa")
    assunto = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    texto = models.TextField(max_length=1000)


    def __str__(self) -> str:
        return self.nome