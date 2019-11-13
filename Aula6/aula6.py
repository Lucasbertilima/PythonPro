#aula 6 - 13-11-2019
#Lista
# Forma de criar uma lista
# Comenta ctrl k c

#Inicialização de uma variável do tipo lista vazia
lista1 = []
#Inicialização de uma variável lista, com elementos
lista2 = ['Marcela','Nicole','*Matheus',10]
#Lista de inteiros
lista3 = [1,2,3,4,5]
#lista de tipos diferentes
lista4=[1,'Lucas',12.5]
#impressão de listas criadas
print(lista1)
print(lista2)
print(lista3)
#---- Adicionando elementos em uma lista já criada
lista1.append(lista2)
lista1.append(lista3)

#---- Impressão de listas modificadas
print(lista1)
print(lista2)
print(lista3)

#---- Criação de listas com dados vindos da função input
lista_pergunta = [input('Digite seu artista favorito'), input('Digite seu guitarrista favorito')]
print(lista_pergunta)

#---- Recuperando um dado de uma posição especifica da lista
posi = int(input('Digite a posição: '))
print( lista2[posi-1] )