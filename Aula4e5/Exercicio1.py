#Crie um programa que leia 4 notas
#imprima a maior nota
#imprima a menor   
#imprima a média
#imprima se o aluno foi aprovado ou reprovado(media7.0)

n1=float(input('Digite a primeira nota'))
n2=float(input('Digite a segunda nota'))
n3=float(input('Digite a terceira nota'))
n4=float(input('Digite a quarta nota'))

if n1>=n2 and n1>=n3 and n1>=n4:
    print(f'A maior nota é {n1}')
elif n2>=n1 and n2>=n3 and n1>=n4:
    print(f'A maior nota é {n2}')
elif n3>=n1 and n3>=n2 and n3>=n4:
    print(f'A maior nota é {n3}')
elif n4>=n1 and n4>=n2 and n4>=n3:
    print(f'A maior nota é {n4}')
else:
    print('')

if n1<=n2 and n1<=n3 and n1<=n4:
    print(f'A menor nota é {n1}')
elif n2<=n1 and n2<=n3 and n1<=n4:
    print(f'A menor nota é {n2}')
elif n3<=n1 and n3<=n2 and n3<=n4:
    print(f'A menor nota é {n3}')
elif n4<=n1 and n4<=n2 and n4<=n3:
    print(f'A menor nota é {n4}')
else:
    print('')

media = (n1+n2+n3+n4)/4

print(f'A média do aluno é {media}')
if media >=7:
    print('Parabens você foi aprovado')
else:
    print('Você foi reprovado')