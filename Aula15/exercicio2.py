def salvar_bebida(bebida_dicionario):
    arquivo = open('exercicio.txt','a')
    arquivo.write(f"{bebida_dicionario['marca']};{bebida_dicionario['tipo']};{bebida_dicionario['teor']} \n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('exercicio.txt','r')
    for linha in arquivo:
        linha=linha.strip()
        lista_linha=linha.split(';')
        bebidas = {'marca':lista_linha[0],'tipo':lista_linha[1],'teor':lista_linha[2]}
        lista.append(bebidas)
    arquivo.close()
    return lista



marca= input('Digite o nome da marca da bebida')
tipo = input('Qual o tipo da bebida')
teor = input('Informe o teor')
bebidas = {'marca':marca,'tipo':tipo,'teor':teor}
salvar_bebida(bebidas)

for bebida in ler():
    print(f"{bebida['marca']} - {bebida['tipo']} - {bebida['teor']}")


