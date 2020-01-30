import sys
sys.path.append('C:/Users/900145/Documents/PythonPro/Aula37')
from model.model_squad import Squad
from dao.dao_squad import SquadDao
from controller.squadcontroller import SquadController


sc = SquadController()
print(sc.buscar_id(2))

