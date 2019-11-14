#--- Exercicio 3 - foreach
#--- Escreva um programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nome em listas
#--- Imprima 
#       1- O nome dos alunos
#       2- Média do aluno
#       3- Resultado (Aprovado>=7.0)

nomes = []
notas = []
n1=0
n2=1
n3=2
n4=3

for i in range(0,2):
    nomes.append(input(f'Digite o nome do aluno {i+1}'))
    for j in range(0,4):
        notas.append(float(input('Digite uma nota')))
    #     media = media+notas[j]
    # media=media/4
    # medias.append(media)
    # media=0

for aluno in nomes:
    media = (notas[n1]+notas[n2]+notas[n3]+notas[n4])/4
    resultado = 'Reprovado'
    if media >=7:
        resultado ='Aprovado'
    print(f'Aluno: {aluno} - média={media} - Resultado:{resultado}')
    n1 += 4
    n2 += 4
    n3 += 4
    n4 += 4
    
    
