from flask_restful import Resource
from Aula41.Dao.pessoa_dao import PessoaDao

class PessoaController(Resource):
    def __init__(self):
        self.dao = PessoaDao()


    def get(self):
        txt = self.dao.list_all()
        return txt
    def post(self):
        txt = self.dao.insert('')
        return txt
    def put(self):
        txt = self.dao.update('')
        return txt
    def delete(self):
        txt = self.dao.remove(9)
        return txt