CodeChallenge_DataEngineer
Prop�sito
Este desafio tem como objetivo avaliar a forma de resolver problemas do candidato. Portanto, a estrutura e a qualidade do c�digo, bem como as tecnologias e t�cnicas utilizadas v�o dizer muito sobre a metodologia utilizada.

Este desafio avaliar� as seguintes habilidades:
�	Entendimento e processamento de s�ries temporais financeiras.
�	Efici�ncia no armazenamento dos dados 
�	Constru��o de uma API REST que responda �s perguntas-chave, definidas nas especifica��es abaixo
O Desafio
1� Trabalho
1 ) Processar o arquivo retirado do site do Tesouro Nacional. 
2 ) Armazenar as informa��es obtidas da melhor forma poss�vel.
2� Trabalho
	1) Construir uma API REST que execute as fun��es:
�	Adicionar um valor monet�rio a um t�tulo
�	Remover um valor monet�rio de um t�tulo
�	Atualizar um valor monet�rio para um t�tulo espec�fico
�	Mostrar o hist�rico de um t�tulo espec�fico
�	Comparar o hist�rico de dois ou mais t�tulos
�	Buscar valores de venda de um t�tulo em determinado per�odo
�	Buscar valores de resgate de um t�tulo em determinado per�odo
Solu��o Proposta
1.	Tecnologias utilizadas:
a)	GitHub (Social Code Hosting) -
b)	Python 
c)	Django (Web Framework) 
d)	SQLite (Database)


2.	Diagrama da solu��o:
 
a.	API
i.	Instala��o das Tecnologias
pip install Django
pip install httpie
python startproject EasyInvest - Cria-se um projeto chamado �EasyInvest�
python manage.py startapp titulo_tesouro - Cria-se um app �titulo_tesouro�
Em �Easyinvest/setting.py� adicionar em INSTALLED_APPS:
 	'rest_framework',
   	'titulo_tesouro',











ii.	Desenvolvimento da API 
1.	Classe Models.py
 

2.	Classe Serializer.py  
3.	Classe Urls.py � Declara��o das URL referentes a �titulo_tesouro� 
4.	Classe Views.py  

iii.	Execu��o do Servidor
python manage.py makemigrations titulo_tesouro
python manage.py migrate
python manage.py runserver
b.	ETL
i.	Download do Arquivo
Salvar como C:\Series_Temporais_Tesouro_Direto.xlsx










ii.	e iii. -  xlsx_open.py
   



c.	Execu��o das Fun��es
�	Adicionar um valor monet�rio a um t�tulo  
 




�	Remover um valor monet�rio de um t�tulo
 
 
 
�	Atualizar um valor monet�rio para um t�tulo espec�fico
     


typie