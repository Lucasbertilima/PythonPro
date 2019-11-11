nome = input ('Digite seu nome: ')
sobrenome = input('Digite o sobrenome: ')
idade = int(input('Digite sua idade: '))
print(f'Seu nome é {nome} {sobrenome} e sua idade é {idade} anos')

if idade < 18:
    print('Não pode usar mercado tech, para o que presta')
else:
    print('Pode usar mercado tech, para o que é bom')


