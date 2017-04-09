from rest_framework import serializers
from titulo_tesouro.models import titulo_tesouro
from django.db import models     

class titulo_tesouro_Serializer(serializers.ModelSerializer):
    class Meta:
        model = titulo_tesouro
        fields = ('id', 'created','categoria_titulo','mes','ano','acao','valor')

    def create(self, validated_data):
        return titulo_tesouro.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.created = validated_data.get('created', instance.created)
        instance.categoria_titulo = validated_data.get('categoria_titulo', instance.categoria_titulo)
        instance.mes = validated_data.get('mes', instance.mes)
        instance.ano = validated_data.get('ano', instance.ano)
        instance.acao = validated_data.get('acao', instance.acao)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.save()
        return instance
