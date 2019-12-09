#1) o que uma classe tem ? quais as caracteristicas?
###### Atributos  ------ variáveis
#nome,idade,telefone,sexo
#2) o que uma pessoa faz?
###### metodos(função,procedimento)
#Respira,dorme, corre, come,bebe,
#3) Como a pessoa está agora
###### Atributos de estado - Variáveis
#fome,sede,viva,cansada

class Pessoa:
    '''
    Demonstração para aula
    '''
    def __init__(self,nome,idade,telefone,sexo):
        '''
        o __init__ é o motos que irá iniciar as variáveis da classe
        o self é o que irá conectar toda a classe
        '''
        #### Atributos #####
        self.nome=nome
        self.idade=idade
        self.telefone=telefone
        self.sexo=sexo

        self.divida = None
        self.cansada='Não'
        self.viva=True
        self.fome='Não'
        self.sede='Não'

    #Metodos#
    def respira(self,respirar):
        if self.viva == True:
            if respirar == True:
                self.viva = True
            else:
                self.viva = False
    def corre (self,distancia):
        if self.viva:
            if distancia <100:
                self.cansada= 'pouco'
                self.sede= 'pouco'
                self.fome = 'pouco'
            elif distancia >= 100 and distancia <200:
                self.cansada= 'medio'
                self.sede= 'medio'
                self.fome = 'medio'
            elif distancia >= 200:
                self.cansada= 'muito'
                self.sede= 'muito'
                self.fome = 'muito'

    def dorme (self):
        if self.viva:
            self.cansada='não'
    def bebe (self):
        if self.viva:
            self.sede='não'
    def come (self):
        if self.viva:
            self.fome='não'
        

p=Pessoa('Antonio',18,'479966995','m')
p.corre(2000)
p.dorme()
p.come()
p.bebe()
print(f'Nome é {p.nome}')
print(f'Está vivo? {p.viva}')
print(f'Está com fome? {p.fome}')
print(f'Está com sede? {p.sede}')
print(f'Está cansada? {p.cansada}')