#--- Exercício 2 - Dicionários
#--- Escreva um programa que leia os dados de 11 jogadores
#--- Jogador: Nome, Posição, Número, PernaBoa
#--- Crie um dicionario para armazenar os dados
#--- Imprima todos os jogadores

jogador = []

for i in range(0,2):
    jogadores={'Nome':'','Posicao':'','Numero':'','PernaBoa':''}
    jogadores['Nome']=input('Digite o nome do jogador')
    jogadores['Posicao']=input('Digite a posição')
    jogadores['Numero']=int(input('Digite o número do jogador'))
    jogadores['PernaBoa']=input('Qual a perna boa do jogador')
    jogador.append(jogadores)
for nao in jogador:
    print(f"Nome: {nao['Nome']} - Posição: {nao['Posicao']} - Número: {nao['Numero']} - Perna Boa: {nao['PernaBoa']}")