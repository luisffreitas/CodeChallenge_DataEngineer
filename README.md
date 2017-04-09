CodeChallenge_DataEngineer
Propósito
Este desafio tem como objetivo avaliar a forma de resolver problemas do candidato. Portanto, a estrutura e a qualidade do código, bem como as tecnologias e técnicas utilizadas vão dizer muito sobre a metodologia utilizada.

Este desafio avaliará as seguintes habilidades:
•	Entendimento e processamento de séries temporais financeiras.
•	Eficiência no armazenamento dos dados 
•	Construção de uma API REST que responda às perguntas-chave, definidas nas especificações abaixo
O Desafio
1º Trabalho
1 ) Processar o arquivo retirado do site do Tesouro Nacional. 
2 ) Armazenar as informações obtidas da melhor forma possível.
2º Trabalho
	1) Construir uma API REST que execute as funções:
•	Adicionar um valor monetário a um título
•	Remover um valor monetário de um título
•	Atualizar um valor monetário para um título específico
•	Mostrar o histórico de um título específico
•	Comparar o histórico de dois ou mais títulos
•	Buscar valores de venda de um título em determinado período
•	Buscar valores de resgate de um título em determinado período
Solução Proposta
1.	Tecnologias utilizadas:
a)	GitHub (Social Code Hosting) -
b)	Python 
c)	Django (Web Framework) 
d)	SQLite (Database)


2.	Diagrama da solução:
 
a.	API
i.	Instalação das Tecnologias
pip install Django
pip install httpie
python startproject EasyInvest - Cria-se um projeto chamado “EasyInvest”
python manage.py startapp titulo_tesouro - Cria-se um app “titulo_tesouro”
Em “Easyinvest/setting.py” adicionar em INSTALLED_APPS:
 	'rest_framework',
   	'titulo_tesouro',











ii.	Desenvolvimento da API 
1.	Classe Models.py
 

2.	Classe Serializer.py  
3.	Classe Urls.py – Declaração das URL referentes a “titulo_tesouro” 
4.	Classe Views.py  

iii.	Execução do Servidor
python manage.py makemigrations titulo_tesouro
python manage.py migrate
python manage.py runserver
b.	ETL
i.	Download do Arquivo
Salvar como C:\Series_Temporais_Tesouro_Direto.xlsx










ii.	e iii. -  xlsx_open.py
   



c.	Execução das Funções
•	Adicionar um valor monetário a um título  
 




•	Remover um valor monetário de um título
 
 
 
•	Atualizar um valor monetário para um título específico
     


typie