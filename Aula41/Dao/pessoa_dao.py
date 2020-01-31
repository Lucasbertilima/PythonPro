from flask_mysqldb import MySQL

class PessoaDao:
    def __init__(self):
        self.connection = MySQL.connect(host='mysql.topskills.dev',database='topskills01',user='topskills01',passwd='ts2019')
        self.cursor = self.connection.cursor()
    def list_all(self):
        self.cursor.execute("SELECT * FROM 01_MDG_PESSOA")
        pessoas = self.cursor.fetchall()
        return pessoas
    def get_by_id(self,id):
        self.cursor.execute("SELECT * FROM 01_MDG_PESSOA WHERE ID = {}".format(id))
        return f'Listando o dado de id:{id}'
    def insert(self,pessoa):
        return 'Cadastrando uma pessoa '
    def update(self,pessoa):
        return 'Alterando uma pessoa'
    def remove(self,id):
        return F'Removendo a pessoa de id={id}'