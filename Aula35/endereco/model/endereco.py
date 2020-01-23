class Endereco:
    idEndereco = 0
    Logradouro = ''
    Numero = ''
    Complemento = ''
    Bairro = ''

    def exportar_txt(self, lista_endereco):
        # ----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('Aula35/endereco/endereco.txt', 'a') as arquivo:
            # ---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for e in lista_endereco:
                arquivo.write(f"{str(e)}\n")

    def __str__(self):
        return f'{self.idEndereco};{self.Logradouro};{self.Numero};{self.Complemento};{self.Bairro}'