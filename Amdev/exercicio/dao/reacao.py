from exercicio.model.reacao_model import ReacaoModel


class Reacao:
    def __init__(self):
        self.model = ReacaoModel(1,1,1,1)

    def salvar(self,model:ReacaoModel):
        reacao = open('C:/Users/900145/Documents/PythonPro/Amdev/exercicio/arquivos_txt/reacao.txt', 'a')
        self.model.tipo_reacao = 'Like'
        self.model.data_reacao = '15/06/1690'
        self.model.pessoa_id = 0
        self.model.id = 1
        reacao.write(f'{self.model}\n')
        reacao.close()

    def ler(self):
        reacao = open('C:/Users/900145/Documents/PythonPro/Amdev/exercicio/arquivos_txt/reacao.txt', 'r')
        lista = []
        for r in reacao:
            lista.append(r)
        reacao.close()
        return lista

r=Reacao()
r.salvar()
lista = r.ler()
print(lista)