# Aula 7 - 14-11-2019
# Dicionarios

# dicionario = { 'Nome':'Lucas', 'Sobrenome':'Lima' }
# print(dicionario)
# print(dicionario['Sobrenome'])

# nome = 'Lucas'
# lista_notas = [10,20,50,70]
# media = sum(lista_notas) / len(lista_notas)
# situacao:'Reprovado'
# if media >=7:
#     situacao = 'Aprovado'
# dicionario_alunos = {'Nome':nome, 'Lista_notas':lista_notas,'media':media,'Situacao':situacao}

# print(f"Nome {dicionario_alunos['Nome']} - Média {dicionario_alunos['media']} - Situação {dicionario_alunos['Situacao']}")

# dicionario_bandas = {}
# dicionario_bandas['Nome'] = 'Calypso'
# dicionario_bandas['Nome'] = 'Dejavu'


# dicionario = {'Nome':'lucas', 'Sobrenome':'Lima'}
# dicionario[Sobrenome]= 'Berti'
# dicionario['CPF'] = '123.456.789-00'
lista_pessoas = []

dicionario_pessoa={'Nome':'','Sobrenome':'','CPF':'','RG':''}
for i in range(1,11):
    dicionario_pessoa['Nome'] = input('Digite o nome: ')
    dicionario_pessoa['Sobrenome'] = input('Digite o Sobrenome: ')
    dicionario_pessoa['CPF'] = input('Digite o CPF: ')
    dicionario_pessoa['RG'] = input('Digite o RG: ')
    lista_pessoas.append(dicionario_pessoa)

print('')
