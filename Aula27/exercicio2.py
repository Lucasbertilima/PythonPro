# Aula 21 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como defult ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10)

a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.




lista = embaralhar(2,10,2)

print(lista)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).
if lista[0] is lista[1]:
    print(f'É a mesma lista')
elif lista[0] == lista[1]:
    print(f'As listas são iguais')
else:
    print(f'São listas diferentes diferentes')

# 2) Qual é o maior valor destas duas listas 
if max(lista[0])>max(lista[1]):
    print(f'O maior número das duas listas é {max(lista[0])}')
elif max(lista[1])>max(lista[0]):
    print(f'O maior número das duas listas é {max(lista[1])}')
else:
    print(f'As listas são iguais')

# 3) Qual é o maior valor de cada lista
print(f'Maior da primeira lista {max(lista[0])}')
print(f'Maior da segunda lista {max(lista[1])}')


# 4) Há o número 10 dentro da lista[0]?
if 10 in lista[0]:
    print('Sim')
else:
    print('Não')


# 5) Há o número 20 dentro da lista[1]?
if 20 in lista[1]:
    print('Sim')
else:
    print('Não')


# 6) Quantos números da lista[0] tem dentro da lista[1]?
e=0
for i in lista[0]:
    if i in lista[1]:
        e = e+1

print(f'Tem {i} elementos da lista[0] na lista[1]')


# 7) Mostre os números da lista[0] que estão dentro da lista[1]
for i in range(0,10):
    if lista[0][i] in lista[1]:
        print(f'{lista[0][i]} está na lista[1]')

# 8) Mutliplique a soma da lista[0] com cada item da lista[1]

for i in range(0,10):
    print(f'Soma {sum(lista[0])} * {lista[1][i]} = {sum(lista[0])*lista[1][i]}')


# 9) Faça uma divizão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!
a = max(max(lista[0]),max(lista[1])) // min(min(lista[0]),min(lista[1]))
print(a)
if a in lista[0]:
    print('Na lista[0]')
elif a in lista[1]:
    print('Na lista[1]')
else:
    print('Em nenhuma')

# 10) Ferifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]

if max(lista[0]) in lista[1]:
    print('O maio número da lista[0] está na lista[1]')
else:
    print('O maio número da lista[0] não está na lista[1]')

if min(lista[1]) in lista[0]:
    print('O menor número da lista[1] está na lista[0]')
else:
    print('O maio número da lista[1] não está na lista[0]')