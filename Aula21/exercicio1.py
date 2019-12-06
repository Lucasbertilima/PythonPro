# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.
op = 'n'
i=True
j=True
while op != 's':
    while i ==True:
        try:                 
            n1= int(input('Digite um número'))
        except ValueError:                             
            print('Erro! Digite um número inteiro')
        else:
            i=False
                
    while j == True:                                                        
        try:                                                
            n2=int(input('Digite um número'))
        except ValueError:
            n2=int(input('Você tem que digitar um número inteiro'))
        else:
            j=False
                                                                         
                                                                        
    print(f'Soma de {n1} + {n2} = {n1+n2}')
    print(f'subtração de {n1} - {n2} = {n1-n2}')
    try:
        print(f'divisão de {n1} / {n2} = {n1/n2}')
    except ZeroDivisionError:
        print('Não da de dividir por zero')
    print(f'multiplicação de {n1} * {n2} = {n1*n2}')
    op=input('Deseja sair? s ou n')
                                                                         
                                                                   
                                                                     
# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.
                                                                         
#################### até aqui tudo bem! ########################## 
                                                                       
# 3 - faça um tratamento de exceção para que ao digitar o valor que  
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.