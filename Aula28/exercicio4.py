# Aula 28 - 17-12-2019
# Listas

# DICA!!!!
# Procurem primeiro o padrão que estas listas vão apresentar! Depois de encontrado, faça o uso da linguagem
# para facilitar na hora de codar!


lista1 = [['frutas','verduras','legumes','preço'],
         ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
         ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha','cebolinha'],
         ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
         [ [10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
           [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55] 
         ]
        ]


lista2 = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]

# 1) Faça um dicionário com a lista1 onde cada elemento esteja junto com o seu respectivo
# preço. (Dica: Use a indexação e fatiamento para ajudar)
tipo = lista1[0]
lista_frutas=[]
lista_verduras=[]
lista_legumes=[]
for i in range(0,7):
    dicio = {lista1[0][0]:lista1[1][i],lista1[0][3]:lista1[4][0][i]}
    lista_frutas.append(dicio)
    dicio = {lista1[0][1]:lista1[2][i],lista1[0][3]:lista1[4][1][i]}
    lista_verduras.append(dicio)
    dicio = {lista1[0][2]:lista1[3][i],lista1[0][3]:lista1[4][2][i]}
    lista_legumes.append(dicio)

lista_tudo = []
lista_tudo.append(lista_frutas)
lista_tudo.append(lista_verduras)
lista_tudo.append(lista_legumes)
print(lista_frutas)
print(lista_legumes)
print(lista_verduras)
# 2) Com o dicionário, imprima os seguintes valores:
# 2.1) Preço do feijão
print(lista_legumes[0])

# 2.2) Preço da cebolinha
print(lista_verduras[5])
# 2.3) Preço da Alface lisa
print(lista_verduras[1])
# 2.4) Preço do Abacaxi
print(lista_frutas[1])
# 2.5) Preço do feijão branco.
print(lista_legumes[4])
# 3) Com a lista1 qual seria a média dos valores das frutas, verduras e legumes?
print(f'Soma frutas {sum(lista1[4][0])}')
print(f'Media frutas {sum(lista1[4][0])/len(lista1[4][0])}')

print(f'Soma frutas {sum(lista1[4][1])}')
print(f'Media frutas {sum(lista1[4][1])/len(lista1[4][1])}')

print(f'Soma frutas {sum(lista1[4][2])}')
print(f'Media frutas {sum(lista1[4][2])/len(lista1[4][2])}')
# 4) Com a lista 1, Qual é o maior e menor valor das frutas, verduras e legumes?
print(f'O menor valor das frutas é {min(lista1[4][0])}')
print(f'O maior valor das frutas é {max(lista1[4][0])}')

print(f'O menor valor dos legumes é {min(lista1[4][1])}')
print(f'O maior valor dos legumes é {max(lista1[4][1])}')

print(f'O menor valor das verduras é {min(lista1[4][2])}')
print(f'O maior valor das verduras é {max(lista1[4][2])}')

# 5) Adicione no cabeçalho da lista1 (entre o legumes e preço) a "roupa". Aṕos adicione de forma que fique 
# com a lista coerente 7 roupas e os seus preços.

lista1[0].insert(3,'roupa')
print(lista1)
roupas = ['roupa1','roupa2','roupa3','roupa4','roupa5','roupa6','roupa7']
preco = [50.0,67.24,190.50,99.99,67.00,45.54,250.50]
lista1.insert(4,roupas)
lista1[5].insert(3,preco)
print(lista1)
# 6) Salve esta lista em um arquivo .txt de moque que cada linha tenha o item e seu preço. 
lista_frutas=[]
lista_verduras=[]
lista_legumes=[]
lista_roupas = []
for i in range(0,7):
    dicio = {lista1[0][0]:lista1[1][i],lista1[0][4]:lista1[5][0][i]}
    lista_frutas.append(dicio)
    dicio = {lista1[0][1]:lista1[2][i],lista1[0][4]:lista1[5][1][i]}
    lista_verduras.append(dicio)
    dicio = {lista1[0][2]:lista1[3][i],lista1[0][4]:lista1[5][2][i]}
    lista_legumes.append(dicio)
    dicio = {lista1[0][3]:lista1[4][i],lista1[0][4]:lista1[5][2][i]}
    lista_roupas.append(dicio)
lista_tudo = []
lista_tudo.append(lista_frutas)
lista_tudo.append(lista_verduras)
lista_tudo.append(lista_legumes)
lista_tudo.append(lista_roupas)
# print(lista_frutas)
# print(lista_legumes)
# print(lista_verduras)

# arquivo = open('Aula28/arquivo.txt','w')
# for lista in lista_tudo:
#   for linha in lista:
#     arquivo.write(f'{linha}\n')
  

# arquivo.close()
# 7) Com a lista2, crie uma lista com dicionário onde cada dicionário é um cadastro de uma pessoa.
lista2 = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]
lista_pessoas = []
for i in range(0,7):
  dicio = {lista2[0]:lista2[1][i],lista2[2]:lista2[3][i],lista2[4]:lista2[5][i],lista2[6]:lista2[7][i]}
  lista_pessoas.append(dicio)
print(lista_pessoas)
# 8) Organize a lista2, retirando o cabeçalho e junte os dados de modo que cada cliente ocupe uma lista. Após, salve os dados
# em um arquivo .txt 
cabecalho = [lista2[0],lista2[2],lista2[4],lista2[6]]
lista2_organizada = []
for i in range(0,7):
  b = [lista2[1][i],lista2[3][i],lista2[5][i],lista2[7][i]]
  lista2_organizada.append(b)
print(lista2_organizada)
arquivo = open('Aula28/arquivo.txt','w')
for i in lista2_organizada:
  arquivo.write(f'{i[0]};{i[1]};{i[2]};{i[3]}\n')
arquivo.close()
# 9) Criando uma fila. Uma fila é uma estrutura de dados onde o primeiro item que entra é o ultimo que sai. Resumindo, o item novo
# entra no indice 0 da lista e sai pelo ultimo indice. 
# Ex:
# >>> []
# >>> [1]
# >>> [2,1]
# >>> [3,2,1]
# >>> [3,2]
# >>> [3] 

# Crie um programa que adiciona novos clientes em uma fila e conforme vai atendendo, remova-os da fila do caixa da loja.
nomes=['nome1','nome2','nome3','nome4','nome5']
fila = []
for i in nomes:
  fila.insert(0,i)
  print(fila)
for i in range(5,0,-1):
  fila.pop()
  print(fila)

# 10) Criando uma pilha. Uma pilha é uma estrutura de dados onde o primeiro que entra é o ultimo a sair. Resumindo,
# Os elementos são adicionados e removidos no mesmo lado da lista.
# Ex:
# >>> []
# >>> [1]
# >>> [1,2]
# >>> [1,2,3]
# >>> [1,2]
# >>> [1] 

# Crie um programa em que adicione os novos números na pilha. Após some eles removendo da pilha.
numeros = [0,1,2,3,4,5]
pilha = []
for i in range(0,6):
  pilha.append(numeros[i])
  print(pilha)
for i in range(6,0,-1):
  pilha.pop()
  print(pilha)