import MySQLdb

from Aula41.Model.pessoa_model import PessoaModel

class PessoaDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='localhost',database='aula41',user='root',passwd='')
        self.cursor = self.connection.cursor()
    def list_all(self):
        self.cursor.execute("SELECT * FROM pessoa")
        pessoas = self.cursor.fetchall()
        lista_pessoas = []
        for p in pessoas:
            pessoa = PessoaModel(p[1],p[2],p[3],p[0])
            lista_pessoas.append(pessoa.__dict__)
        return lista_pessoas
    def get_by_id(self,id):
        self.cursor.execute("SELECT * FROM pessoa WHERE idPessoa = {}".format(id))
        pessoa = self.cursor.fetchone()
        p = PessoaModel(pessoa[1],pessoa[2],pessoa[3],pessoa[0])
        return p.__dict__
    def insert(self,pessoa:PessoaModel):
        self.cursor.execute(""" INSERT INTO pessoa
        (Nome, Sobrenome, Idade)
        VALUES
        ('{}','{}',{})
        """.format(pessoa.nome,pessoa.sobrenome,pessoa.idade))
        self.connection.commit()
        id= self.cursor.lastrowid
        pessoa.id = id
        return pessoa.__dict__

    def update(self,pessoa:PessoaModel):
        self.cursor.execute("""UPDATE pessoa
        SET
            Nome = '{}',
            Sobrenome = '{}',
            Idade = {}
        WHERE idPessoa = {}
        """.format(pessoa.nome,pessoa.sobrenome,pessoa.idade,pessoa.id))
        self.connection.commit()
        return pessoa.__dict__
    def remove(self,id):
        self.cursor.execute("DELETE FROM pessoa WHERE idPessoa={}".format(id))
        self.connection.commit()
        return 'Pessoa removida de id= {id}'.format(id)