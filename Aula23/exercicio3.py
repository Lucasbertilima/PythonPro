# Aula 22 - 10-12-2019
# # Como Tratar e Trabalhar Erros!!!

# Dica: O mais importante é conseguir fazer! Não importa como chegou ao resultado e sim o resultado!

# Dica2: na função .open() você pode escolher entre 'r' para ler, 'w' para sobrescrever e criar um 
# arquivo novo ou o 'a' que é abreveativo de append, onde ele inclui linha no final do arquivo.
# Você sabia que o 'r', 'w' e o 'a' são string que podem ser passadas via variável exemplo:

# atributo = 'r'
# nome_arquivo = 'cadastro'
# arquivo.open(f'exercicio/{nome_arquivo}.txt',atributo)



# 1) Crie uma classe cadastro.
# Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastro numa lista com dicionários.

# 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
# 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode 
# se repetir.
# 3) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
# 4) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
#
#  Observação: Use o try/finaly para abrir e fechar os arquivos. Veja na aula 21- Ecessões como é!


class cadastro:
    def __init__(self):
        self.codigo = None
        self.nome= None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone =None
        self.cliente = []

    def guardar(self):
        arquivo = open('Aula23/cadastro2.txt','r')
        for linha in arquivo:
            linha= linha.strip().split(';')
            dic_cliente= {'codigo':linha[0],'nome':linha[1],'idade':linha[2],'sexo':linha[3],'email':linha[4],'telefone':linha[5]}
            self.cliente.append(dic_cliente)
        arquivo.close()

    def cadastro(self):
        numero=int(input('Qual o codigo do cliente'))
        for pessoa in self.cliente:
            if int(pessoa['codigo']) == numero:
                print('Codigo já existe')
                numero=int(input('Informe outro codigo de cliente'))
        self.codigo = numero
        self.nome=input('Qual o nome do cliente')
        self.idade = int(input('Qual a idade'))
        self.sexo = input('Informe o sexo')
        self.email = input('Informe o email')
        self.telefone = int(input('Informe o telefone'))

    def salvar(self):
        dic_cliente= {'codigo':self.codigo,'nome':self.nome,'idade':self.idade,'sexo':self.sexo,'email':self.email,'telefone':self.telefone}
        self.cliente.append(dic_cliente)
        arquivo = open('Aula23/cadastro2,1.txt','w')
        for pessoa in self.cliente:
            for dado in pessoa:
                arquivo.write(dado)
        arquivo.close



c=cadastro()
c.guardar()
c.cadastro()
c.salvar()
