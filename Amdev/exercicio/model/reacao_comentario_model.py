

class ReacaoComentarioModel:
    def __init__(self,id=None,reacao_id=None,comentario_id=None):
        self.id = id
        self.reacao_id = reacao_id
        self.comentario_id = comentario_id

    def as_dict(self):
        return {'id':self.id,'reacao_id':self.reacao_id,'comentario_id':self.comentario_id}

    def criar(self,dado):
        dado = dado.split(';')
        self.id = dado[0]
        self.reacao_id = [1]
        self.comentario_id = [2]