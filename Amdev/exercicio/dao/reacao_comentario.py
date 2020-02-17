from exercicio.model.reacao_comentario_model import ReacaoComentarioModel

class ReacaoComentario:

    def salvar(self):
        self.reacao = open('C:/Users/900145/Documents/Amdev/exercicio/arquivos_txt/reacao_comentario.txt', 'a')
        self.reacao.write('2;5;1')
        self.reacao.close()

    def ler(self):
        reacao = open('C:/Users/900145/Documents/Amdev/exercicio/arquivos_txt/reacao_comentario.txt','r')
        model = ReacaoComentarioModel()
        model.criar(reacao.__str__())
        model.as_dict()
        reacao.close()
        return model