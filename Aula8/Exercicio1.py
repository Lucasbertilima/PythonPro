#--- Exercício 1 -
#--- Escreva programa que leia os dados de cerveja
#--- Cerveja: Marca, Tipo, IBU, ABV, EBV, Volume
#--- Crie um dicionário para armazenar os dados
#--- Imprima os dados do dicionário (Não dicionário completo)

Marca = input('Digite o nome da marca de cerveja')
Tipo = input('Digite o tipo de cerveja')
IBU = float(input('Informe o IBU da cerveja'))
ABV = float(input('Informe o ABV da cerveja'))
EBC = float(input('Informe o EBV da cerveja'))
volume = float(input('Qual o volume da cerveja'))

Cerveja = {'Marca':Marca, 'Tipo':Tipo, 'IBU':IBU, 'ABV':ABV, 'EBC':EBC, 'Volume': volume}

print(f"Marca: {Cerveja['Marca']} - Tipo: {Cerveja['Tipo']} - IBU: {Cerveja['IBU']} - ABV: {Cerveja['ABV']} - EBC: {Cerveja['EBC']} - Volume: {Cerveja['Volume']}")