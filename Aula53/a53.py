#ORM
#---- SqlAlchemy
#---- pip install sqlalchemy

#---- Conector do Mysql
#---- Instalação do conector do Mysql
#---- pip install mysql-connector-python

from Aula53.dao.cargo_dao import CargoDao

from Aula53.model.cargo_model import CargoModel

dao = CargoDao()
#cargos = dao.list_all()
#cargo = CargoModel()
#cargo.Nomecargo= 'bombeiro'
#cargo.Cargahoraria = 40
#cargo.Salario = 3000
#a=dao.insert(cargo)
#print(a)
#for i in a:
#    print(i)

dao.update()
cargos = dao.list_all()
print(cargos)

#dao.delete(4)
#cargos = dao.list_all()
#print(cargos)
#a = dao.get_by_id(3)
#print(a)