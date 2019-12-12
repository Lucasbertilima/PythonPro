# Aula 21 - 12-12-2019


# Cliente.....

# Crie uma classe cliente.
# Use os seguintes atributos: codigo cliente(int), nome, idade(int), telefone, email, endereço
# Use o seguinte atributo de estado: crédito em R$, saldo R$, 
#                                    cliente_devedor(True/False)
# O atributo cliente_devedor deve ser True toda vez que o saldo negativo for menor 
# ou igual ao crédito. 
# Para o atributo cliente_devedor voltar a ser False o cliente deve pagar sua divida
# ficando com o saldo igual a 0 ou positivo.



# Como metodo use:
class Cliente:
    def __init__(self,codigo, nome, idade, telefone, email, endereco):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

        self.credito = -0
        self.saldo = 0
        self.cliente_devedor = False



    def atualizar (self):
        '''
        Este metodo serve para atualizar o cadastro do cliente. 
        Os dados que podem ser atualizados são: 
        nome, idade(int), telefone, email, endereço
        '''
        self.nome = input('Digite o novo nome ')
        self.idade = int(input('Nova idade '))
        self.telefone = input('Novo telefone ')
        self.email = input('Novo email ')
        self.endereco = input('Novo endereço')

    def limite_credito(self,valor):
        '''
        O crédito é o valor máximo que o cliente pode ter de saldo negativo.
        Este metodo altera o valor tanto para aumentar o crédito quanto para 
        diminuir ou eliminar o crédito.
        Este valor deve ser passado como número negativo (ex: -50.00) para o atributo
        credito
        Se diminuir o crédito (exemplo de -50 para -10) e o 
        cliente ficar com o saldo menor que o cédito (exemplo saldo = -20 e cédito -10)
        o cliente_devedor fica True
        Se o cliente_devedor estiver True, o crédito pode ser diminuido porem não aumentado.
        
        '''
        valor = valor- (valor*2)
        if self.cliente_devedor == True:
            if valor > 0 :
                self.credito += valor
            else:
                pass
        else:
            self.credito += valor
        
        if self.saldo < self.credito:
            self.cliente_devedor = True
        

        

    def dinheiro(self,valor):
        '''
        Este metodo serve para adicionar/remover valor em R$ para o atributo saldo para 
        o cliente.
        Esta função revebe o valor como parametro. Se o valor for positivo, o saldo
        aumenta, se o valor for negativo o saldo diminui. 
        
        O cliente não pode ter seu saldo menor que o crédito. Então se o valor exceder
        deve retornar False e a operação fica cancelada.
        (Exemplo: limite do cartão de crédito)
        Caso o valor não exceda o crédito a operação será realizada, o valor do saldo
        irá diminuir e deve retornar True
        Se o cliente_devedor estiver True o dinheiro só poderá receber valores positivos.
        Se o cliente_devedor estiver True e o cliente depositar dinheiro suficiente para
        o saldo ficar maior ou igual a 0 o cliente_devedor deve ser alterado para False.
        '''
        
        if self.saldo < self.credito:
            print('Limite do cartão de crédito')
        else:
            self.saldo += valor
    def __eq__(self,valor):
        '''
        Este metodo deve comparar se o valor do código do cliente é igual ao valor.
        Se positivo ele retorna True caso contrário retorna False
        '''
        return self.codigo == valor

    def __srt__(self):
        '''
        Este metodo deve retornar uma string com todos os dados do cliente.
        Use f-string para interpolar o texto com as variáveis
        '''
        texto = f'''{self.codigo};{self.nome};{self.idade};{self.telefone};{self.email};{self.endereco}'''
        return texto



if __name__ == "__main__":

    '''
    Use este if para fazer os testes com a classe.
    Este if pergunta se este arquivo está sendo executado diretamente.
    Caso positivo o código será executado.
    '''
    pass
codigo = int(input('Informe o codigo'))
nome = input('Digite o novo nome ')
idade = int(input('Nova idade '))
telefone = input('Novo telefone ')
email = input('Novo email ')
endereco = input('Novo endereço')

c=Cliente(codigo,nome,idade,telefone,email,endereco)
salario = float(input('Qual o salario ?'))
credito = float(input('Qual o limite de credito que o cliente tem?'))
c.limite_credito(credito)
c.dinheiro(salario)
