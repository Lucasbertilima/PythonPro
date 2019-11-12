#2 -
#Mercado tech ----
#Solicitar Nome do funcionario
#Solicitar idade
#Informar se o funcionario pode adquirir produtos alcoolicos

nome=input('\n Digite o nome do funcionario')
idade=int(input('\n Digite a idade'))

if idade >= 18:
    print(f'\n O funcionario {nome} pode adquirir produtos alcoolicos')
else:
    print(f'\n O funcionario {nome} é menor de idade, não pode adquirir produtos alcoolicos')

#3 -
#Cadastro Produtos Mercado Tech
#Solicitar o nome do produto
#Solicitar a categoria do produto(Alcoolicos e Não Alcoolicos)
#Exibir o produto cadastrado

nomep=input('\n Digite o nome do produto')
categ= int(input('\n Digite a categoria: 1- Alcoolico 2- não Alcoolico'))

if categ == 1:
    print(f'\n O nome do produto é {nomep} e ele é Alcoolico')
elif categ ==2:
    print(f'\n O nome do produto é {nomep} e ele é não Alcoolico')
else:
    print('\n Categoria não existe')