from django.db import models


#criação da classe titulo_tesouro
class titulo_tesouro(models.Model):
	#atributos dessa classe
    created = models.DateTimeField(auto_now_add=True)
    categoria_titulo = models.CharField(max_length=58)
    mes = models.IntegerField()
    ano = models.IntegerField()
    acao = models.CharField(max_length=7)
    valor = models.FloatField()

    class Meta:
        ordering = ('created',)