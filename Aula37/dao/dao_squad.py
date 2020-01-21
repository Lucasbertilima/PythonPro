import MySQLdb
import sys
sys.path.append('C:/Users/900145/Documents/PythonPro/Aula37')
from model.model_squad import Squad
class SquadDao:
    conexao = MySQLdb.connect(host='localhost', database='Exercicio', user='root', passwd='')
    cursor = conexao.cursor()
    def __init__(self):
        self.Nome = ''
        self.Descricao = ''
        self.NumeroPessoas = 0
        self.LinguagemBackEnd = ''
        self.FrameworkFrontEnd = ''

    def listar(self):
        comando = "SELECT * FROM squad;"
        self.cursor.execute(comando)
        resultado=self.cursor.fetchall()
        return resultado

    def buscar_id(self,id):
        comando = f"SELECT * FROM squad WHERE id = {id};"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self,squad=Squad()):
           comando = f"""
                       INSERT INTO Squad
                       (Nome,Descricao,NumeroPessoas,LinguagemBackEnd,FrameworkFrontEnd)
                       VALUES
                       ('{squad.Nome}','{squad.Descricao}','{squad.NumeroPessoas}','{squad.LinguagemBackEnd}','{squad.FrameworkFrontEnd}');
                       """
           self.cursor.execute(comando)
           self.conexao.commit()
    def alterar(self,squad=Squad()):
           comando = f"""UPDATE squad " \
                     SET
                     Nome = '{squad.Nome}'
                     Descricao = '{squad.Descricao}'
                     NumeroPessoas = '{squad.NumeroPessoas}'
                     LinguagemBackEnd = '{squad.LinguagemBackEnd}'
                     FrameworkFrontEnd = '{squad.FrameworkFrontEnd}'
                     ;
                     """
           self.cursor.execute(comando)
           self.conexao.commit()

    def deletar(self,id):
           comando = f"""
                   DELETE FROM squad
                   WHERE id={id}
     
                   """



squad = SquadDao()
print(squad.listar())