#Aula 4
#Fazer um programa que leia 2 números
#Realize as 4 operações matematicas
#Imprima o resultado
#Diga qual número é o maior

n1 = int(input('\n Digite um número'))
n2 = int(input('\n Digite outro número'))

som=n1+n2
sub=n1-n2
mult=n1*n2
div=n1/n2

print(f'\n O resultado da soma é {som}, da subtração é {sub}, da multiplicação é {mult} e a divisão é {div}.') 

if n1 > n2:
    print(f'\n {n1} é maior que {n2}')
elif n2>n1:
    print(f'\n {n2} é maior que{n1}')
else:
    print(f'Os números {n1} e {n2} são iguais')