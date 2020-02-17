

class Reacao_post:
    def ler(self):
        reacao = open('C:/Users/900145/Documents/Amdev/exercicio/arquivos_txt/reacao_post.txt', 'r')
        lista = []
        for r in reacao:
            lista.append(r)
        reacao.close()
        return lista

    def salvar(self):
        reacao = open('C:/Users/900145/Documents/Amdev/exercicio/arquivos_txt/reacao_post.txt', 'a')
        reacao.write('1;1;1;2')
        reacao.close()

