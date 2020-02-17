from flask_restful import Resource

from exercicio.dao.reacao import Reacao


class Reacao_Controller(Resource):
    def __init__(self):
        self.dao = Reacao()

    def get(self):
        return self.dao.ler()