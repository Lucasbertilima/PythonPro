from flask_restful import Resource

from exercicio.dao.reacao_post import Reacao_post


class Reacao_Post_Controller(Resource):
    def __init__(self):
        self.dao = Reacao_post()

    def get(self):
        return self.dao.ler()