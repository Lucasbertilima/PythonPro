import sys
sys.path.append('C:/Users/900145/Documents/PythonPro/Aula37')
from dao.dao_squad import SquadDao
from model.model_squad import Squad
class SquadController:
    dao = SquadDao()

    def listar(self):
        lista= []
        tuplas = self.dao.listar()
        for s in tuplas:
            squad= Squad()
            squad.id=s[0]
            squad.Nome=s[1]
            squad.Descricao=s[2]
            squad.NumeroPessoas=s[3]
            squad.LinguagemBackEnd=s[4]
            squad.FrameworkFrontEnd=s[5]
            lista.append(squad)
        return lista
    def buscar_id(self,id):
        s=self.dao.Buscar_id(id)
        squad=Squad()
        squad.id = s[0]
        squad.Nome = s[1]
        squad.Descricao = s[2]
        squad.NumeroPessoas = s[3]
        squad.LinguagemBackEnd = s[4]
        squad.FrameworkFrontEnd = s[5]
        return squad

    def salvar(self):
        return self.dao.salvar()

    def alterar(self):
        return self.dao.alterar()

    def deletar(self):
        return self.dao.deletar()
