import flask_mysqldb
from flask_mysqldb import MySQLdb 
from contextlib import closing

__dados = {'host':"mysql.topskills.study",
            'database':'topskills01',
            'user':'topskills01',
            'passwd': 'ts2019',
            'port':3306}

def cadastrar(nome,idade):
    with closing(MYSQLdb.connect(**__dados)) as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO topskills01.abioluz(nome,idade) VALUES ('{nome}',{idade});")
        conn.commit()

def consultarAll():
    with closing(MYSQLdb.connect(**__dados)) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Lucas')
        print('\nSó uma linha: ',cursor.fetchone())
        print('\nVarias linhas',cursor.fetchall())

for i in range(3):
    nome = input('Digite Nome: ')
    idade = int(input('Digite a idade: '))
    cadastrar(nome,idade)
consultarAll()
