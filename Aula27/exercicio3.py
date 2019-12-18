# Aula 21 - 16-12-2019
# Metodos da lista

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_inpura_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import lista_simples_impura
from geradorlista import embaralhar
from geradorlista import embaralhar_int_str_hard
from geradorlista import binario







# Exercícios baseados do livro Pense em Python.

# 1) Escreva uma função chamada nested_sum que receba a lista de listas de números
# inteiros (lista1), retorne uma lista única e print a soma de todos os elementos.
# Por exemplo:
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> lista = nested_sum(t)
# 21
# >>> lista
# [1, 2, 3, 4, 5, 6]

lista1 = [lista_simples_int() ,lista_simples_int(), lista_simples_int()]
def nested_sum(lista):
    lista = lista
    lista1 = []
    for i in lista:
        for j in i:
            lista1.append(j)
    return lista1

listinha = nested_sum(lista1)
# print(sum(listinha))
# print(listinha)

# 2) Com as seguintes listas, transforme em uma string para poder gravar (futuramente) em um arquivo!

lista_cadastro = ['codigo', 'cpf', 'nome_completo', 'data_de_nascimento',
                  'estado', 'cidade', 'cep', 'bairro', 'rua', 'numero', 'complemento']

lista_cadastrados = ['1', '11111111111', 'João Carlos', '12/12/90',
                  'SC', 'Camboriú', '8833', 'Tabuleiro', 'Cerejeiras', '45', 'ap 101']

lista_cadastrados1 = ['2', '22222222222', 'Paulo Roberto', '23/01/89',
                  'SC', 'Blumenau', '99999', 'Velha', '7 de setembro', '55', '']
str_cadastro =';'.join(lista_cadastro)
str_cadastrados1 = ';'.join(lista_cadastrados)
str_cadastrados2 = ';'.join(lista_cadastrados1)


# 3) Com as seguintes lista, transforme em uma string para poder gravar (futuramente) em um arquivo!

lista_cadastros = [['1', 'Arnaldo', '23', 'm', 'alexcabeludo2@hotmail.com', '014908648117'], ['2', 'Haroldo', '44', 'f', 'baratarebelde@gmail.com', '050923172729'], ['3', 'Pilar', '50', 'm', 'wanderson10sp@gmail.com', '018937341049'], ['4', 'Suzete Salvador', '45', 'f', 'eladiomp2@yahoo.com.br', '056928409823'], ['5', 'Riane', '37', 'f', 'orkutzimpower@terra.com.br', '018916004377'], ['6', 'Waldir', '34', 'f', 'nandah.s2@bol.com.br', '058903756441'], ['7', 'Lilian', '22', 'f', 'arydoido@gmail.com', '031958621596'], ['8', 'Matilde', '20', 'm', 'eu_kaka_@hotmail.com', '012941959390'], ['9', 'Samanta', '19', 'm', 'carro.tuning@yahoo.com.br', '028964480437'], ['10', 'Margarida', '30', 'm', 'paraaconta.08@hotmail.com', '047903547580'], ['11', 'Evelyn', '31', 'm', 'joaosilvaticudo@gmail.com', '053958638386'], ['12', 'Alessio', '29', 'm', 'w.nill02@gmail.com', '033961294774'], ['13', 'Yolanda', '25', 'm', 'patty_karen2005@hotmail.com', '027903312626'], ['14', 'Germana', '33', 'f', 'jarlinhatopdelinhagv@hotmail.com', '053964603415'], ['15', 'Helio', '33', 'f', 'juh.slim@gmail.com', '046997316461'], ['16', 'Liége', '21', 'f', 'gledsonlds@hotmail.com', '056992948431'], ['17', 'Yan', '42', 'm', 'lucapratto@yahoo.com.br', '016963562866'], ['18', 'Silvain', '50', 'f', 'hie.s2@hotmail.com', '021963399433'], ['19', 'Brian', '33', 'f', 'juliagabrielle06@hotmail.com', '027962676732'], ['20', 'Deoclides', '40', 'f', 'patriciamascena@gmail.com', '012961047979'], ['21', 'Jaqueline', '32', 'm', 'aninha183@hotmail.com', '014958997782'], ['22', 'Rosamaria', '45', 'f', 'j_leosao@hotmail.com', '026944672627'], ['23', 'Carla', '42', 'm', 'jhasdfjo@hotmail.com', '046976625208'], ['24', 'Aida Santos', '30', 'f', 'nayara.cristinap@hotmail.com', '034920819199'], ['25', 'Thomas', '19', 'm', 'jfdslinda@bol.com.br', '030974027667'], ['26', 'Naiara', '23', 'm', 'darknees_666@ig.com.br', '018976696717'], ['27', 'Karyne', '17', 'm', 'garotosonhador_1@hotmail.com', '054984689319'], ['28', 'Alenis Dias', '43', 'f', 'vi_vi_cristinaf@hotmail.com', '034980886309'], ['29', 'Grace', '38', 'm', 'amandakell@uol.com.br', '041932906720'], ['30', 'Zacarias', '31', 'm', 'loca.som@hotmail.com', '041926007066']]
cont = len(lista_cadastros)




# 4) Crie uma função que solicite 5 nomes e retorne uma lista com todos eles

def solicita():
    nomes = []
    for i in range(0,5):
        nome = input('Informe um nome')
        nomes.append(nome)
    return nomes
Nomes =solicita()

# 5) Com a lista "Nomes", feita no exercicio 4 (anterior) faça uma cópia para 'Nomes2' e adicione 
#o nome "Pedro Paulada" no "Nomes" e "Paulo Cacetada" no "Nomes2"
Nomes2 = Nomes.copy()
Nomes.append('Pedro Paulada')
Nomes2.append('Paulo Cacetada')


# 6) Com a lista 'lista_aninhada' faça uma cópia e nomeie como 'lista_aninhada_2'. Na lista_aninhada
# adicione ao lado do número 9 o número 10. Na lista_aninhada_2 adicione ao lado do número 8 a frase 
# "Aqui não pode ter o número 10!"
import copy

lista_aninhada = [1,2,3,[4,5,[7,[9],8],6]]
lista_aninhada2 = copy.deepcopy(lista_aninhada)
lista_aninhada[3][2][1].insert(9,10)
lista_aninhada2[3][2].insert(8,"Aqui não pode ter o número 10!")



# 7) Continuando o exercicio, adicione a lista Nomes (exercicio 4) na lista_aninhada entre os números
# 2 e o 3. Na lista_aninhada_2 adicione a "Pedro Pedroca" entre os números 4 e 5. 
# Adicione na lista_aninhada, entre os números 1 e 2, a frase 'um, dois' e na lista_aninhada_2, 
# entre os números 1 e 2 a frase 'Adiciono qualquer coisa em qualquer lugar nesta lista!'
lista_aninhada.insert(2,Nomes)
lista_aninhada2[3].insert(1,'Pedro Pedroca')
lista_aninhada.insert(1,'um, dois')
lista_aninhada2.insert(1,'Adiciono qualquer coisa em qualquer lugar nesta lista!')


# 8) Com a lista1, ordene os números de maior para menor!

# lista1 = lista_simples_int(100)
# lista1.sort(reverse=True)



# 9) Com a lista2, ordene os números de menor para maior!

# lista2 = lista_simples_int(100)
# lista2.sort(reverse=False)

# 10) Usando o metodo, adicione a lista1 e lista2 (já ordenadas) na lista0.

# lista0 = []
# lista0.append(lista1)
# lista0.append(lista2)

# 11) Ordene a lista0 e diga qual é o maior valor, menor valor e em quais das listas (lista1 ou lista2)
# estes pertencem.
# lista0.sort()
# if max(lista0[0]) > max(lista0[1]):
#     print('O maior valor está na lista0[0]')
# elif max(lista0[1]) > max(lista0[0]):
#     print('O maior valor está na lista0[1]')

# if min(lista0[0]) < min(lista0[1]):
#     print('O menor valor está na lista0[0]')
# elif min(lista0[1]) < min(lista0[0]):
#     print('O menor valor está na lista0[1]')


# 12) Com a lista_aninhada e lista_aninhada2, do exercicio 7, remova todas as alterações que nelas foram
# colocadas. Salve os dados removidos em uma lista e imprima na tela cada item em uma linha
# usando o f-string (use o .pop() )
# print(lista_aninhada)
# print(lista_aninhada2)
lista_aninhada[5][2][1].pop()
lista_aninhada.pop(1)
lista_aninhada.pop(3)
lista_aninhada.pop(2)
lista_aninhada2.pop(1)
lista_aninhada2[3].pop(1)
lista_aninhada2[3][2].pop(3)
# print(lista_aninhada)
# print(lista_aninhada2)

# 13) Remova, usando o .remove(), os seguintes itens destas listas:
# 13.1) cpf da lista_cadastro
# 13.2) camboriú da lista_cadastrados
# 13.3) Paulo Roberto da lista_cadastrados1
# 13.4) rua 
# 13.5) 8833 
# 13.6) Velha
# 13.7) João Carlos
# 13.8) 11111111111
# 13.9) cidade
# 13.10) data_de_nascimento


lista_cadastro = ['codigo', 'cpf', 'nome_completo', 'data_de_nascimento',
                  'estado', 'cidade', 'cep', 'bairro', 'rua', 'numero', 'complemento']
lista_cadastro.remove('cpf')
lista_cadastro.remove('cidade')
lista_cadastro.remove('data_de_nascimento')

print(lista_cadastro)

lista_cadastrados = ['1', '11111111111', 'João Carlos', '12/12/90',
                  'SC', 'Camboriú', '8833', 'Tabuleiro', 'Cerejeiras', '45', 'ap 101']
lista_cadastrados.remove('Camboriú')
lista_cadastrados.remove('Cerejeiras')
lista_cadastrados.remove('8833')
lista_cadastrados.remove('João Carlos')
lista_cadastrados.remove('11111111111')

print(lista_cadastrados)

lista_cadastrados1 = ['2', '22222222222', 'Paulo Roberto', '23/01/89',
                  'SC', 'Blumenau', '99999', 'Velha', '7 de setembro', '55', '']
lista_cadastrados1.remove('Paulo Roberto')
lista_cadastrados1.remove('Velha')

print(lista_cadastrados1)

# 14) Com a lista_fusao mostre com f-strig e o metodo .index() a posição dos seguintes elementos:
# 14.1) cidade
# 14.2) João Carlos
# 14.3) Camboriú
# 14.4) 12/12/90
# 14.5) 99999
# 14.6) nome_completo
# 14.7) 22222222222
# 14.8) Tabuleiro
# 14.9) numero

lista_fusao = ['codigo', 'cpf', 'nome_completo', 'data_de_nascimento',
                  'estado', 'cidade', 'cep', 'bairro', 'rua', 'numero', 'complemento',
                  '1', '11111111111', 'João Carlos', '12/12/90',
                  'SC', 'Camboriú', '8833', 'Tabuleiro', 'Cerejeiras', '45', 'ap 101',
                  '2', '22222222222', 'Paulo Roberto', '23/01/89',
                  'SC', 'Blumenau', '99999', 'Velha', '7 de setembro', '55', '']
a=lista_fusao.index('cidade',0,32)
b=lista_fusao.index('João Carlos',0,32)
c=lista_fusao.index('Camboriú',0,32)
d=lista_fusao.index('12/12/90',0,32)
e=lista_fusao.index('99999',0,32)
f=lista_fusao.index('nome_completo',0,32)
g=lista_fusao.index('22222222222',0,32)
h=lista_fusao.index('Tabuleiro',0,32)
i=lista_fusao.index('numero',0,32)
print(f'Posição de cidade {a}')
print(f'Posição de João Carlos {b}')
print(f'Posição de Camboriú {c}')
print(f'Posição de 12/12/90 {d}')
print(f'Posição de 99999 {e}')
print(f'Posição de nome_completo {f}')
print(f'Posição de 22222222222 {g}')
print(f'Posição de Tabuleiro {h}')
print(f'Posição de numero {i}')


# 15) Usando o metodo .index(), Crie uma função que localize a posição dos seguintes nomes: 
# Germana, Deoclides, Zacarias, Karyne, Helio, Silvain, Aida Santos
# Esta função deve receber como parametro a lista_cadastros e o nome. Deve retornar uma lista contendo
# o endereço do nome na lista_cadastros. 
# Exemplo:

# >>> lista = localize(lista_cadastros,'Alenis Dias')
# >>> lista_cadastros[ lista[0] ][ lista[1] ]
# 'Alenis Dias'

# Dica: Use o tratamento de ecessões para evitar erro ao procurar um indice que não existe!



lista_cadastros = [['1', 'Arnaldo', '23', 'm', 'alexcabeludo2@hotmail.com', '014908648117'], ['2', 'Haroldo', '44', 'f', 'baratarebelde@gmail.com', '050923172729'], ['3', 'Pilar', '50', 'm', 'wanderson10sp@gmail.com', '018937341049'], ['4', 'Suzete Salvador', '45', 'f', 'eladiomp2@yahoo.com.br', '056928409823'], ['5', 'Riane', '37', 'f', 'orkutzimpower@terra.com.br', '018916004377'], ['6', 'Waldir', '34', 'f', 'nandah.s2@bol.com.br', '058903756441'], ['7', 'Lilian', '22', 'f', 'arydoido@gmail.com', '031958621596'], ['8', 'Matilde', '20', 'm', 'eu_kaka_@hotmail.com', '012941959390'], ['9', 'Samanta', '19', 'm', 'carro.tuning@yahoo.com.br', '028964480437'], ['10', 'Margarida', '30', 'm', 'paraaconta.08@hotmail.com', '047903547580'], ['11', 'Evelyn', '31', 'm', 'joaosilvaticudo@gmail.com', '053958638386'], ['12', 'Alessio', '29', 'm', 'w.nill02@gmail.com', '033961294774'], ['13', 'Yolanda', '25', 'm', 'patty_karen2005@hotmail.com', '027903312626'], ['14', 'Germana', '33', 'f', 'jarlinhatopdelinhagv@hotmail.com', '053964603415'], ['15', 'Helio', '33', 'f', 'juh.slim@gmail.com', '046997316461'], ['16', 'Liége', '21', 'f', 'gledsonlds@hotmail.com', '056992948431'], ['17', 'Yan', '42', 'm', 'lucapratto@yahoo.com.br', '016963562866'], ['18', 'Silvain', '50', 'f', 'hie.s2@hotmail.com', '021963399433'], ['19', 'Brian', '33', 'f', 'juliagabrielle06@hotmail.com', '027962676732'], ['20', 'Deoclides', '40', 'f', 'patriciamascena@gmail.com', '012961047979'], ['21', 'Jaqueline', '32', 'm', 'aninha183@hotmail.com', '014958997782'], ['22', 'Rosamaria', '45', 'f', 'j_leosao@hotmail.com', '026944672627'], ['23', 'Carla', '42', 'm', 'jhasdfjo@hotmail.com', '046976625208'], ['24', 'Aida Santos', '30', 'f', 'nayara.cristinap@hotmail.com', '034920819199'], ['25', 'Thomas', '19', 'm', 'jfdslinda@bol.com.br', '030974027667'], ['26', 'Naiara', '23', 'm', 'darknees_666@ig.com.br', '018976696717'], ['27', 'Karyne', '17', 'm', 'garotosonhador_1@hotmail.com', '054984689319'], ['28', 'Alenis Dias', '43', 'f', 'vi_vi_cristinaf@hotmail.com', '034980886309'], ['29', 'Grace', '38', 'm', 'amandakell@uol.com.br', '041932906720'], ['30', 'Zacarias', '31', 'm', 'loca.som@hotmail.com', '041926007066']]
def localiza(lista_cadastros,nome):
    lista = lista_cadastros
    nomes=nome
    for i in nomes:
        for j in range(0,30):
            try:
                a = lista[j].index(i,0,6)
            except ValueError:
                pass
            else:
                print(f'A posição do nome {i} é {a+1} na lista {j+1}')
nome = ['Germana', 'Deoclides', 'Zacarias', 'Karyne', 'Helio', 'Silvain', 'Aida Santos']
# localiza(lista_cadastros,nome)

# 16) Conte na lista1 a quantidade dos seguintes valores (use o f-string):
lista1 = lista_simples_int(10000)
# 16.1) 4529
print(f'4529 aparece {lista1.count(4529)} vezes')
# 16.2) 29
print(f'29 aparece {lista1.count(29)} vezes')
# 16.3) 1107
print(f'1107 aparece {lista1.count(1107)} vezes')
# 16.4) 7927
print(f'7927 aparece {lista1.count(7927)} vezes')
# 16.5) 6967
print(f'6967 aparece {lista1.count(6967)} vezes')
# 16.6) 5964
print(f'5964 aparece {lista1.count(5964)} vezes')
# 16.7) 8893
print(f'8893 aparece {lista1.count(8893)} vezes')
# 16.8) 3972
print(f'3972 aparece {lista1.count(3972)} vezes')
# 16.9) 10
print(f'10 aparece {lista1.count(10)} vezes')
# 16.10) 8548
print(f'8548 aparece {lista1.count(8548)} vezes')
# 16.11) 8214
print(f'8214 aparece {lista1.count(8214)} vezes')
# 16.12) 169
print(f'169 aparece {lista1.count(169)} vezes')
# 16.13) 6214
print(f'6214 aparece {lista1.count(6214)} vezes')
# 16.14) 15
print(f'15 aparece {lista1.count(15)} vezes')
# 16.15) 4937
print(f'4937 aparece {lista1.count(4937)} vezes')
# 16.16) 9909
print(f'9909 aparece {lista1.count(9909)} vezes')
# 16.17) 3412
print(f'3412 aparece {lista1.count(3412)} vezes')
# 16.18) 6306
print(f'6306 aparece {lista1.count(6306)} vezes')
# 16.19) 306
print(f'306 aparece {lista1.count(306)} vezes')


lista1 = lista_simples_int(10000)


###################### .reverse() ######################

# 17) Um numero binário, localizado em uma lista 'listabin', necessita ser convertido em número decimal.
# Faça uma função que converta o número binário e retorne o número em decimal. Imprima na tela
# o número binário e o resultado. (use o .reverte())


listabin = binario()
def converte(listabin):
    listabin = listabin
    lista=[]
    for numeros in listabin:
        numero = int(numeros)
        lista.append(numero)
    return lista

numero = converte(listabin)
print(listabin)
print(numero.reverse())
# 18) com as seguintes listas, imprima elas e .reverte() suas posições. Some as posições e retorne a lista com
# as somas.
# Exemplo:
# >>> lista1        = [42,3, 1, 4]
# >>> lista_reversa = [4, 1, 3, 42]
# >>> lista_soma    = [46,4, 4, 46]

# 18.1) lista1
lista1 = lista_simples_int(8)
print(lista1)
print(f'Reversa {lista1.reverse()}')
# 18.2) lista2
lista2 = lista_simples_int(8)

# 18.3) lista3
lista3 = lista_simples_int(8)

# 18.4) lista4
lista4 = lista_simples_int(8)

# 18.5) lista5
lista5 = lista_simples_int(8)

# 18.6) lista6
lista6 = lista_simples_int(8)

# 18.7) lista7
lista7 = lista_simples_int(8)

# 18.8) lista8
lista8 = lista_simples_int(8)

# 18.9) lista9
lista9 = lista_simples_int(8)

# 18.10) lista10
lista10 = lista_simples_int(8)

# 18.11) lista11
lista11 = lista_simples_int(8)

# 18.12) lista12
lista12 = lista_simples_int(8)

# 18.13) lista13
lista13 = lista_simples_int(8)

# 18.14) lista14
lista14 = lista_simples_int(8)

# 18.15) lista15
lista15 = lista_simples_int(8)

# 18.16) lista16
lista16 = lista_simples_int(8)

# 18.17) lista17
lista17 = lista_simples_int(8)

# 18.18) lista18
lista18 = lista_simples_int(8)

# 18.19) lista19
lista19 = lista_simples_int(8)




# 19) Com um comando .clear()  apague as seguintes informações:
# 19.1) apague toda a lista
lista_aninhada = [1, 2, 3, [4, 5, [1, 2, 3, [4, 5, [7, [9], 8], 6]], 6]]

# 19.2)  apague somente: [4, 5, [1, 2, 3, [4, 5, [7, [9], 8], 6]], 6]
lista_aninhada = [1, 2, 3, [4, 5, [1, 2, 3, [4, 5, [7, [9], 8], 6]], 6]]

# 19.3) [4, 5, [7, [9], 8], 6]
lista_aninhada = [1, 2, 3, [4, 5, [1, 2, 3, [4, 5, [7, [9], 8], 6]], 6]]

# 19.4)  [7, [9], 8]
lista_aninhada = [1, 2, 3, [4, 5, [1, 2, 3, [4, 5, [7, [9], 8], 6]], 6]]

# 19.5) 5,6
lista_aninhada = [[1,2],[3,4],[5,6],[7,8],[9,10]]

# 19.6) 9,10
lista_aninhada = [[1,2],[3,4],[5,6],[7,8],[9,10]]
