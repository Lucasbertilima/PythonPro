# Criar um programa para o cadastro de cliente
# deve pedir os seguintes dados:
#Codigo do cliente, CPF, Nome completo, Data de nascimento,
#Estado, Cidade, CEP, Bairro, Rua, Número da casa, complemento. 
def cadastro_cliente(numero):
    cliente =   ['Codigo_cliente', 'CPF', 'Nome_completo', 'Data_de_nascimento',
                'Estado', 'Cidade', 'CEP', 'Bairro', 'Rua', 'Número_da_casa', 'complemento']

    lista = []
    for j in range(numero):
        dicionario = {}
        for i in cliente:
            dicionario[i]=input(f'{i}:')
        lista.append(dicionario)
    return lista
numero = int(input('Digite o número de cadastros:'))
lista_cadastro = cadastro_cliente(numero)
print(lista_cadastro)
