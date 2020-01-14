# referencia ao mysql

from flask_mysqldb import MySQLdb
conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user = 'topskills01', passwd = 'ts2019' )

conexao2= MySQLdb.connect(host='localhost', database='aulabd', user = 'root', passwd = '' )

cursor = conexao2.cursor()
cursor.execute('SELECT * FROM pessoa AS P JOIN endereco AS E ON P.enderecoid = E.idendereco;')
pessoas = cursor.fetchall()
for p in pessoas:
    print(p)