#--- Exercicio 3 - foreach
#--- Escreva um programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nome em listas
#--- Imprima 
#       1- O nome dos alunos
#       2- Média do aluno
#       3- Resultado (Aprovado>=7.0)
n1=float
n2=float
n3=float
n4=float
nomes = []
notas = [n1,n2,n3,n4]

for i in range(0,2):
    nomes.append(input('Digite seu nome'))
    for j in range(0,4):
        notas.append(float(input('Digite uma nota')))

for i in range(0,2):
    print(nomes[i])
    media =   
    print(f'{media}')

