import sys
sys.path.append('C:/Users/900145/Documents/PythonPro/Aula37')
from dao.dao_squad import SquadDao

class SquadController:
    dao = SquadDao()

    def Listar(self):
        return self.dao.listar()

    def buscar_id(self,id):
        return self.dao.buscar_id(id)

    def salvar(self):
        return self.dao.salvar()

    def alterar(self):
        return self.dao.alterar()

    def deletar(self):
        return self.dao.deletar()
