# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um metodo que leia 5 valores inteiros e retorne uma lista.
# Esta função deve ter tratamento de excessão evitando erro ValueError.

# 2 - Com a lista retornada, faça a multiplicação por 5 e salve o resultado
# em outra lista.

# Imprima a lista resultante

def ler():
    numeros=[]
    for i in range(5):
        while True:
            try:
                n1=int(input(f'{i+1} Digite um número inteiro'))
            except ValueError:
                print('Erro! Digite um número inteiro')
            else:
                numeros.append(n1)
                break        
    return numeros

lista = ler()
lista2=[]
for i in lista:
    n=i
    n=n*5
    lista.append(n)

print (lista)
          