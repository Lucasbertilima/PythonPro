import MySQLdb
from model.endereco import Endereco

class EnderecoDb:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')

    cursor = conexao.cursor()

    def listar_todos(self):

        comando_select = 'SELECT * FROM endereco'
        self.cursor.execute(comando_select)
        resultado = self.cursor.fetchall()
        lista_enderecos_classe = self.converter_tabela_classe(resultado)
        return lista_enderecos_classe

    def listar_por_id(self,id):
        select_id = f'SELECT * FROM endereco WHERE id = {id}'
        self.cursor.execute(select_id)
        resultado = self.cursor.fetchone()
        return resultado

    def converter_tabela_classe(self, lista_tuplas):

        lista_enderecos = []
        for p in lista_tuplas:

            p1 = Endereco()

            p1.idEndereco = p[0]
            p1.Logradouro = p[1]
            p1.Numero= p[2]
            p1.Complemento = p[3]
            p1.Bairro = p[4]
            lista_enderecos.append(p1)
        return lista_enderecos