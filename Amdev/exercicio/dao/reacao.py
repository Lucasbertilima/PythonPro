

class Reacao:
    def salvar(self):
        reacao = open('C:/Users/900145/Documents/Amdev/exercicio/arquivos_txt/reacao.txt', 'a')
        reacao.write('2;3;1')
        reacao.close()

    def ler(self):
        reacao = open('C:/Users/900145/Documents/Amdev/exercicio/arquivos_txt/reacao.txt', 'r')
        lista = []
        for r in reacao:
            lista.append(r)
        reacao.close()
        return lista