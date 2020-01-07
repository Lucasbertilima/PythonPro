# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)

class cliente:
    def __init__(self,dadobruto):
        self.dado_bruto = dadobruto
        self.codigo_cliente= None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None
    def var(self):
        e = self.dado_bruto
        e = e.split(';')
        self.codigo_cliente = int(e[0])
        self.nome = e[1]
        self.idade = int(e[2])
        self.sexo = e[3]
        self.email = e[4]
        self.telefone = int(e[5])


c=cliente(dadobruto)
c.var()
print(f'código: {c.codigo_cliente}\nNome: {c.nome}\nIdade: {c.idade}\nSexo: {c.sexo}\nEmail: {c.email}\nTelefone: {c.telefone}')

