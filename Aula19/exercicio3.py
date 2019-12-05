# Aula 19 - 04-12-2019
# Lista com for e metodos
from exercicio1 import cadastroHBSIS

# Como comer um gigante.... é com um pedaço de cada vez.
# Na hora de fazer este exercicio, atentar para 

# Com o arquivo de cadastro.txt onde possui os seguintes dados: codigo cliente, nome, idade, sexo, e-mail e telefone
# 1 - Crie um metodo que gere e retorne uma lista com bibliotecas com os dados dos clientes
def retorna():
    lista = []
    arquivo = open('Aula19/cadastro.txt','r')
    for l in arquivo:
        l=l.strip()
        lista_linha=l.split(';')
        dados= {'codigo':lista_linha[0],'nome':lista_linha[1],'idade': lista_linha[2],'sexo':lista_linha[3],'e-mail':lista_linha[4],'telefone':lista_linha[5]}
        lista.append(dados)
    arquivo.close()
    return lista
# 2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
# Esta função tambem retornar uma lista com a biblioteca dos maiores de idades.
def separa(cadastroHBSIS):
    maior = []
    for i in range(0,7):
        if int(cadastroHBSIS[7][i])>= 18:
            arquivo = open('Aula19/maior.txt','a')
            arquivo.write(f"{cadastroHBSIS[1][i]};")
            arquivo.write(f"{cadastroHBSIS[3][i]};") 
            arquivo.write(f"{cadastroHBSIS[5][i]};")
            arquivo.write(f"{cadastroHBSIS[7][i]}\n")
            arquivo.close()
            dicio_maior = {cadastroHBSIS[0]:cadastroHBSIS[1][i],cadastroHBSIS[2]:cadastroHBSIS[3][i],cadastroHBSIS[4]:cadastroHBSIS[5][i],cadastroHBSIS[6]:cadastroHBSIS[7][i]}
            maior.append(dicio_maior)

        else:
            arquivo = open('Aula19/menor.txt','a')
            arquivo.write(f"{cadastroHBSIS[1][i]};")
            arquivo.write(f"{cadastroHBSIS[3][i]};")
            arquivo.write(f"{cadastroHBSIS[5][i]};")
            arquivo.write(f"{cadastroHBSIS[7][i]}\n")
            arquivo.close()
    return maior

maior=separa(cadastroHBSIS)
#print(maior)
lista=retorna()
#print(lista)



# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente
def conta():
    for i in lista:
        if i['sexo'] =='f':
            arquivo=open('Aula19/homens.txt','a')
            arquivo.write(f"{i['codigo']};")
            arquivo.write(f"{i['nome']};")
            arquivo.write(f"{i['idade']};")
            arquivo.write(f"{i['sexo']};")
            arquivo.write(f"{i['e-mail']};")
            arquivo.write(f"{i['telefone']}\n")
            arquivo.close()
        else:
            arquivo=open('Aula19/mulheres.txt','a')
            arquivo.write(f"{i['codigo']};")
            arquivo.write(f"{i['nome']};")
            arquivo.write(f"{i['idade']};")
            arquivo.write(f"{i['sexo']};")
            arquivo.write(f"{i['e-mail']};")
            arquivo.write(f"{i['telefone']}\n")
            arquivo.close()

    
            
    

# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1
def consulta():
    codigo = int(input('Digite o codigo do cliente'))
    for l in lista:
        if l['codigo'] == codigo:
            print(f' o Cliente é  ')
        else:
            pass
    
consulta()
#  4.1 - A pesquisa deve aparecer uma frase para as seguintes condições:
#           Mulheres até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!""
#           Mulheres acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor alegria! O seu 
#                                            cruch vai adorar!"
#           Mulheres acima de 18:  "Olá {nome}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico
#                                                com o dobro de sabor!!!"
#           Homens até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!""
#           Homens acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor Corriga de carros!  
#                                          A sua amada vai adorar!"
#           Homens acima de 18:  "Olá {nome}! Já experimentou nossa cerveja? alto teor alcoolico
#                                                com o dobro do amargor!!!"
#      Lembre-se: É importante que apareça a frase. Pois a mesma será encaminhada por e-mail pela equipe de marketing