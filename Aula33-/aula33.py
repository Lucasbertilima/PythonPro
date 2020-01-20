#Importando biblioteca Mysqldb
import MySQLdb
#Configurar a conexão
conexao = MySQLdb.connect(host='localhost', database='aulabd', user = 'root', passwd = '')
#Salva o cursor da conexão em uma variável
cursor = conexao.cursor()
lista_pessoas= []
#Criação do comando SQL e passado para o cursor
comando_sql_select = "SELECT * FROM Pessoa"
cursor.execute(comando_sql_select)

resultado = cursor.fetchall()
for p in resultado:
    dicionario_pessoa = {'id':0,'Nome': '', 'Sobrenome': '', 'Idade': 0, 'idendereco': 0}
    dicionario_pessoa['id'] = p[0]
    dicionario_pessoa['Nome'] = p[1]
    dicionario_pessoa['Sobrenome'] = p[2]
    dicionario_pessoa['Idade'] = p[3]
    dicionario_pessoa['idendereco'] = p[4]
    lista_pessoas.append(dicionario_pessoa)

with open('aula.txt','a') as arquivo:
    for p in lista_pessoas:
        arquivo.write(f"{p['id']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['idendereco']}")
