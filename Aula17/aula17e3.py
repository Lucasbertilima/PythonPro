# Faça um programa que leia um número inteiro de 1 a 100 no teclado e mostre se você acertou
# ou o número digitado é maior ou menor.
#Quando você acertar o programa deve ser finalizado

from random import randint
aleatorio = randint(1,100)
print(aleatorio)

n1=int(input('Digite um número'))
while n1 != aleatorio:
    if n1>aleatorio:
        print('O número digitado é maior')
        n1=int(input('Digite um número'))
    elif n1<aleatorio:
        print('O número digitado é menor')
        n1=int(input('Digite um número'))
print('Acertou')
