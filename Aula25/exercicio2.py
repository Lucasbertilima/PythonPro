# Aula 21 - 12-12-2019
# 
# Cadastro de cliente.
from exercicio1 import Cliente
# Crie uma classe para cadastrar cliente. 
# Para guardar os clientes cadastrado, utilize a classe feita no
# exercicio1.py importando ela.

# Como atributo, utilize uma lista vazia para guardar os clientes.

class CadastroCliente:
    def __init__(self):
        self.clientes = []

    def ler_arquivo(self,nome_arquivo):
        '''
        Este metodo serve para ler um arquivo .txt que deve possuir os 
        dados de clientes cadastrados.
        Vai receber como parametro o nome do arquivo (nome_arquivo) a ser 
        lido.
        Os dados lidos devem ser atribuidos a classe pessoa.
        '''
        arquivo = open(f'Aula25/{nome_arquivo}.txt','r')
        for linha in arquivo:
            linha.split(';')
            dic = {'codigo':linha[0],'nome':linha[1],'idade':linha[2],'telefone':linha[3],'email':linha[4],'endereço':linha[5]}
            self.clientes.append(dic)
        arquivo.close()

    def cadastro_cliente(self):
        '''
        Este metodo é utilizado para cadastrar um cliente.
        Os dados devem ser aplicados em uma classe pessoa.
        O codigo cliente não pode se repetir e deve estar na sequencia númerica
        (novos clientes recebem os ultimos numeros)
        Neste caso se faz necessário adicionar linha no arquivo de texto com o metodo
        gravar adicionando os novos clientes (use o atributo 'a')
        '''

        codigo = len(self.clientes)+1
        nome = input('Informe o nome do cliente')
        idade = int(input('Informe a idade do cliente'))
        telefone = input('Informe o telefone do cliente')
        email = input('Qual o email do novo cliente')
        endereço = input('Qual o endereço do cliente')


    def pesquisa_codigo(self,codigo):
        '''
        Neste metodo é feito a pesquisa do cliente, mostrando os 
        dados do mesmo.
        No caso perguntará se vai querer alterar os dados do cliente.
        Se sim, altere e encaminhe para o metodo gravar.
        Lembrando que no caso de alteração, será necessário fazer a gravação de
        todos os dados usando o atributo 'w'.
        '''
        for cliente in self.clientes:
            if codigo == cliente['codigo']:
                print(f'Codigo {cliente['codigo']}\n nome {cliente['nome']}\n idade {cliente['idade']}\n telefone {cliente['telefone']}\n email {cliente['email']}\n endereço {cliente['endereço']}')
                a = input('Deseja alterar os dados do cliente? [s/n]').upper()
                if a == 'S':
                    gravar()

    def gravar(self,nome_arquivo,atributo):
        '''
        Este é responsável por gravar os dados dos clientes.
        use o atributo 'w' para sobrescrever o arquivo e o
        atributo 'a' para adicionar linha.
        o parametro nome_arquivo é o nome do arquivo em que se deseja gravar.
        '''
        
        arquivo = open(f'{nome_arquivo}',f'{atributo}')
        arquivo.close()