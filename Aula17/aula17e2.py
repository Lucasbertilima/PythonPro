# Faça um menu interativo que tenha Cadastro da banda, cadastro do album , cadastro da musica, sair
# o menu deve ser executado até que se escolha a opção sair.
# Cada opção deve ser mostrada
#Quando selecionado a opção sair, deverá aparecer na tela as informações das bandas cadastradas,albuns e musicas

menu='''
############################################################################
#                               Cadastro faixas                            #
############################################################################
1- Cadastro de banda
2- Cadastro de album
3- Cadastro da musica
4- Sair'''
bandas = []
albuns=[]
musicas=[]
op=input(menu)
while True:
    if op == '1':
        banda=input(print('Digite o nome da banda'))
        bandas.append(banda)
        op=input(menu)
    elif op =='2':
        album=input(print('Digite o nome do album'))
        albuns.append(album)
        op=input(menu)
    elif op=='3':
        musica=input(print('Digite o nome da musica'))
        musicas.append(musica)
        op=input(menu)
    elif op=='4':
        print(f'lista de bandas {bandas}\nlista de albuns {albuns}\nlista de musicas {musicas}')
        break
    else:
        print('Opção invalida')
        op=input(menu)



