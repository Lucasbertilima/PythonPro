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


def lista_festa(lista_entrada):
    lista_mulheres=[]
    lista_homens=[]
    for pessoa in lista_entrada:
        if int(pessoa['idade'])>=18:
            if pessoa['sexo'] =='f':
              lista_mulheres.append(pessoa)  
            else:
                lista_homens.append(pessoa)
    salvar(lista_homens,'homens')
    salvar(lista_mulheres,'mulheres')
def salvar(lista,nome):
    arquivo = open(f'Aula18/{nome}.txt','a')
    for pessoa in lista:
        texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['sexo']};{pessoa['idade']};"
        arquivo.write(texto)
    arquivo.close()

def consulta(lista_consulta_funcao,numero):
    for lista_consulta in lista_consulta_funcao:
        if int(lista_consulta['codigo']) == numero:
            if int(lista_consulta['idade']) >=18:
                if lista_consulta['sexo']=='f':
                    print(f"Nome:{lista_consulta['nome']} valor ingresso:R$15,00")
                else:
                    print(f"Nome:{lista_consulta['nome']} valor ingresso:R$35,00")
            else:
                print('Não pode entrar!')

lista1=ler()
lista_festa(lista1)

while True:
    a=int(input('Digite um número'))
    consulta(lista1,a)
