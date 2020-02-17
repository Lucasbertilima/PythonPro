from flask_restful import Resource

from exercicio.dao.reacao_comentario import ReacaoComentario


class Reacao_Comentario_Controller(Resource):
    def __init__(self):
        self.dao = ReacaoComentario()

    def get(self):
        return self.dao.ler()
