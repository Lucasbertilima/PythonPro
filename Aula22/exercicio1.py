# Crie uma classe cliente 
#1)Deve ter como atributos: codigo,cpf,nome,idade,sexo
#2)Como metodos: receber salario, comprar, pagar divida
#3) Quando recebe aumenta o dinheiro na carteira
#4) Quando compra aumenta os bens e diminui o dinheiro na carteira
#5) se comprar e não tiver dinheiro o suficiente deve diminuir o dinheiro da carteira e aumentar a a divida
#6) Para pagar a divida tem que ter dinheiro o suficiente na carteira
#7) Atributos de estado: dinheiro na carteira, divida,bens

class cliente:
    def __init__(self,codigo,cpf,nome,idade,sexo):
        self.codigo=codigo
        self.cpf=cpf
        self.nome=nome
        self.idade=idade
        self.sexo=sexo

        self.dinheiro=0 
        self.divida=0 
        self.bens=0

    def receber_salario(self,salario):
        self.dinheiro = self.dinheiro + salario
    def comprar(self,valor):
        if valor>self.dinheiro:
            self.divida= self.dinheiro-valor
            self.dinheiro= 0
            self.bens=self.bens+1
        else:
            self.dinheiro=self.dinheiro - valor
            self.bens=self.bens+1
    def pagar_divida(self):
        if self.divida>self.dinheiro:
            print('Você não tem dinheiro para pagar a divida')
        else:
            self.dinheiro=self.divida+self.dinheiro
            self.divida=0
                
        

nome='Lucas'
cpf=70234936
idade=17
sexo='m'
salario= float(input('Informe seu salario'))
c=cliente(1,cpf,nome,idade,sexo)

c.receber_salario(salario)
print(f'Seu dinheiro atual é {c.dinheiro}')
op=int(input('Deseja comprar algo? 1-Sim 2-Não'))
while op == 1:
    c.comprar(float(input('Qual o valor da compra')))
    break
else:
    pass

print(f'Você tem {c.dinheiro} na carteira')
print(f'Você possui {c.bens} bens')
print(f'Sua divida atual é {c.divida}')
print('Recebendo novo salario')
c.receber_salario(salario)
if c.divida != 0 :
    i=int(input('Deseja pagar essa divida 1-Sim 2-Não'))
    if i ==1:
        c.pagar_divida()
    else:
        pass

print(f'Você tem {c.dinheiro} na carteira')
print(f'Você possui {c.bens} bens')
print(f'Sua divida atual é {c.divida}')
