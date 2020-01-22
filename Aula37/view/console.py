import sys
sys.path.append('C:/Users/900145/Documents/PythonPro/Aula37')
from model.model_squad import Squad
from dao.dao_squad import SquadDao
from controller.squadcontroller import SquadController

squad = Squad()

squad.Nome='Squad1'
squad.Descricao='ert'
squad.NumeroPessoas=5
squad.LinguagemBackEnd= 'python'
squad.FrameworkFrontEnd= 'flask'

print(squad)

sc = SquadController()
lista = sc.listar()
print(lista)

