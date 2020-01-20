import sys
sys.path.append('C:/Users/900145/Documents/PythonPro/Aula35/endereco')
from controller.endereco_controller import EnderecoController

ec = EnderecoController()

for e in ec.listar_todos():
    print(e)