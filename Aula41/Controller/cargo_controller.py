from flask_restful import Resource
from flask import request

from Aula41.Model.cargo_model import CargoModel
from Aula41.Dao.cargo_dao import CargoDao
class CargoController(Resource):
    def __init__(self):
        self.dao = CargoDao()
    def get(self,id = None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self):
        nome = request.json['nome']
        horas = request.json['horas']
        salario = request.json['salario']
        cargo = CargoModel(nome,horas,salario)
        msg = self.dao.insert(cargo)
        return msg
    def put(self,id):
        nome = request.json['nome']
        horas = request.json['horas']
        salario = request.json['salario']
        cargo = CargoModel(nome, horas, salario,id)
        msg = self.dao.update(cargo)
        return msg
    def delete(self,id):
        return self.dao.remove(id)

