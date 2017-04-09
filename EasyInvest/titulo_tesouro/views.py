from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from titulo_tesouro.models import titulo_tesouro
from titulo_tesouro.serializers import titulo_tesouro_Serializer

@api_view(['GET', 'POST'])
def titulo_tesouro_list(request, format=None):
    if request.method == 'GET':
        titulo = titulo_tesouro.objects.all()
        serializer = titulo_tesouro_Serializer(titulo, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = titulo_tesouro_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Titulo criado com sucesso.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'UPDATE', 'DELETE'])
def titulo_tesouro_detail(request, pk, format=None):
    try:
        titulo = titulo_tesouro.objects.get(pk=pk)
    except titulo_tesouro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = titulo_tesouro_Serializer(titulo)
        return Response(serializer.data)

    elif request.method == 'UPDATE':
        serializer = titulo_tesouro_Serializer(titulo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Titulo atualizado com sucesso.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        titulo.delete()
        return Response("Titulo deletado")