def salvar_pessoa(pessoa_dicionario):
    arquivo = open('exercicio.txt','a')
    arquivo.write(f"{pessoa_dicionario['nome']};{pessoa_dicionario['sobrenome']};{pessoa_dicionario['idade']} \n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('exercicio.txt','r')
    for linha in arquivo:
        linha=linha.strip()
        lista_linha=linha.split(';')
        pessoas = {'nome':lista_linha[0],'sobrenome':lista_linha[1],'idade':lista_linha[2]}
        lista.append(pessoas)
    arquivo.close()
    return lista


nome = input('Digite seu nome')
sobrenome = input('Digite o sobrenome')
idade=int(input('Digite a idade'))
pessoas = {'nome':nome,'sobrenome':sobrenome,'idade':idade}
salvar_pessoa(pessoas)
for pessoa in ler():
    print(f"{pessoa['nome']} - {pessoa['sobrenome']} - {pessoa['idade']}")

