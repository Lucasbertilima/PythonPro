# aula 17 02/12/2019
# exercicio 1

menu ='''
#######################################################
#              I Festival da cerveja                  #
#######################################################

1 - Cadastro de Cliente
2 - Ver clientes Cadastrados
3 - Cadastro de Produtos
4 - Ver Produtos Cadastrados
5 - Vendas
6 - Relatorio de Vendas
7 - Sair

Digite a opção desejada: '''
op = input(menu)

while True:
    op = input(menu)
    if op =='1':
        print('Cadastro de Cliente')
    elif op=='2':
        print('Ver cliente Cadastrados')
    elif op=='3':
        print('Cadastro de Produtos')
    elif op=='4':
        print('Ver Produtos Cadastrados')
    elif op=='5':
        print('Vendas')
    elif op=='6':
        print('Relatório de Vendas')
    elif op=='7':
        print('Sair')
        break
    else:
        print('Opção invalida')

