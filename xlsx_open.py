from openpyxl.reader.excel import load_workbook
import sqlite3
from datetime import datetime

#   Conectando com o BD e Criando a TABLE 
db = sqlite3.connect('EasyInvest/db.sqlite3')
cur = db.cursor()

#comando parar criar tabela caso não exista, desenvolvido a partir de Models.py
cur.execute('''CREATE TABLE IF NOT EXISTS titulo_tesouro_titulo_tesouro(
                    id               INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT,
                    created          DATETIME     NOT NULL,
                    categoria_titulo VARCHAR (58) NOT NULL,
                    mes              INTEGER      NOT NULL,
                    ano              INTEGER      NOT NULL,
                    acao             VARCHAR (7)  NOT NULL,
                    valor            REAL         NOT NULL
                )''')

#Abrir arquivo de series temporais
wb = load_workbook(filename = 'C:\Series_Temporais_Tesouro_Direto.xlsx')
ws = wb['Planilha1']

#declaração de variaveis auxiliares
i = 0                       #Variavel utilizada para identificar inicio dos valores das series temporais
mes = ""
ano = ""
nome_Serie = []             #Vetor utilizado para registrar nome da serie temporal
nome_Serie.append("blank")
nome_Serie.append("blank")

#python lê célula a célula do arquivo
for row in ws.rows:
    for cell in row:
        i = i + 1      
        valor_Celula = str(cell.value)
        created = str(datetime.now())
        #registra nome da series no vetor
        if "Nome da série" in valor_Celula:
            nome_Serie.append(valor_Celula)
        #após a contagem de 155 células começam os valores corresnpondentes as Series

        #a primeira informação registrada é o mês e ano
        if (i > 155) and i % 14 == 2 :
            mes = valor_Celula[5:-12]
            ano = valor_Celula[:4]

        #em seguida os valores para cada série são registrado
        #primeiras 6 células - series de Vendas
        if (i > 155) and i % 14 > 2 and i % 14 <= 8 :
            nome_SerieTemp = nome_Serie[i%14-1]
            categoria_titulo = nome_SerieTemp[40:]
            acao = "Vendas"
            valor = valor_Celula
            #registramos os valores das series temporais no banco de dados SQLite3 criado
            cur.execute('''INSERT INTO titulo_tesouro_titulo_tesouro(created, categoria_titulo, mes, ano, acao,valor)
                   VALUES(?,?,?,?,?,?)''', (created,categoria_titulo,mes, ano, acao,valor))
        
        #ultimas 6 células - series de Resgates
        elif (i > 155) and (i % 14 > 8 or i % 14 == 0):
            if(i % 14 == 0):
                nome_SerieTemp = nome_Serie[13]
            else:
                nome_SerieTemp = nome_Serie[i%14-1]
            categoria_titulo = nome_SerieTemp[42:]
            acao = "Resgates"
            valor = valor_Celula
            #registramos os valores das series temporais no banco de dados SQLite3 criado
            cur.execute('''INSERT INTO titulo_tesouro_titulo_tesouro(created, categoria_titulo, mes, ano, acao,valor)
                   VALUES(?,?,?,?,?,?)''', (created,categoria_titulo,mes, ano, acao,valor))

#Commit das execuções
db.commit()         

###################################################