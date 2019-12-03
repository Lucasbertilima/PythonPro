# Aula 18 - 03-11-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: codigo, nome, sexo, idade

# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) do que para os homens (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.

# 3 - Faça uma terceira função que ao digitar o código do participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de idade apareça o texto "Entrada Proibida!"

def ler():
    lista_pessoas=[]
    arquivo = open('Aula18/cadastro.txt','r')
    for l in arquivo:
        l=l.strip()
        lista_linha=l.split(';')
        pessoas = {'codigo':lista_linha[0],'nome':lista_linha[1],'sexo':lista_linha[2],'idade':lista_linha[3]}
        lista_pessoas.append(pessoas)
    arquivo.close()
    return lista_pessoas
def salvar(lista_pessoas):
    lista_pessoas=ler()
    lista_homem=[]
    lista_mulher=[]
    for l in lista_pessoas:
        if l['sexo'] =='f':
            lista_mulher.append(lista_pessoas)
            mulher = open ('Aula18/mulheres.txt','w')
            mulher.write(lista_mulher[0])
            mulher.close
        else:
            lista_homem.append(lista_pessoas)
            homem = open ('Aula18/homens.txt','w')
            homem.write(lista_homem[0])
            homem.close
lista_pessoas=ler()
salvar(lista_pessoas)




