# Aula 9 - 19-11-2019
#--- Crie um programa que:
#--- 1 - Leia dois números inteiros
#--- 2 - Calcule a soma entre os dois números atraves de um metodo
#--- 2 - Calcule a subtração entre os dois números atraves de um metodo
#--- 2 - Calcule a multiplicação entre os dois números atraves de um metodo
#--- 2 - Calcule a divisão inteira entre os dois números atraves de um metodo
#--- 2 - Calcule a divisão fracionada entre os dois números atraves de um metodo
#--- 2 - Calcule resto da divisão entre os dois números atraves de um metodo
#--- 2 - Calcule a raiz entre os dois números atraves de um metodo
#--- 2 - Separa os metodos em outro arquivo
from metodos import soma,subtracao,multiplicacao,div_int,divisaof,restodiv,raiz,potencia

n1 = int(input('Digite um número'))
n2 = int(input('Digite um número'))

soma= soma(n1,n2)
sub= subtracao(n1,n2)
mult = multiplicacao(n1,n2)
div= div_int(n1,n2)
divif =divisaof(n1,n2)
restdiv = restodiv(n1,n2)
raiz = raiz(n1,n2)
pot = potencia(n1,n2)
print('='*50,'\n')
print(f'Soma : {soma} \nSubtração : {sub} \nMultiplicação : {mult} \ndivisão inteira : {div} \ndivisão fracionada : {divif} \nresto da divisão : {restdiv}')
print(f'Raiz {n2} de {n1} : {raiz} \nPotencia {n2} de {n1} : {pot}')
print('\n','='*50)
