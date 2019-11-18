#--- Exercicio 1  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia dois números inteiros
#--- Realize as 4 operações matemáticas básicas com os números lidos
#--- Imprima os resultados das operações 
#--- Informe qual número é maior ou se os dois são iguais

# n1 = int(input('Digite o número 1'))
# n2 = int(input('Digite o número 2'))

# print(f'soma {n1}+{n2} = {n1+n2}')
# print(f'subtração {n1}-{n2} = {n1-n2}')
# print(f'soma {n1}*{n2} = {n1*n2}')
# print(f'soma {n1}/{n2} = {n1/n2}')

# if n1>n2:
#     print(f'O número 1 {n1} é maior que {n2}')
# elif n1<n2:
#     print(f'O número 2 {n2} é maior que {n1}')
# else:
#     print('OS números são iguais')


#--- Exercicio 2  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um cliente
#--- Cliente: Nome, Sobrenome, ano de nascimento
#--- Exiba uma mensagem de boas vindas para o cliente
#--- Exiba um menu: Produtos alcoolicos e Produtos não alcoolicos, Sair
#--- Caso o cliente seja menor de idade o item 'produtos alcoolicos' não deve ser exibido
#--- Leia a opção digitada e crie uma tela para cada opção

# Nome = input('Digite o nome')
# sobrenome = input('Digite o sobrenome')
# anonasc =int(input('Qual o ano de nascimento'))
# idade = 2019 - anonasc

# print(f'Seja bem vindo {Nome}')

# if idade>=18:
#     print('='*50,'\n')
#     print(' 1 - Produtos alcoolicos')
#     print(' 2 - Produtos não alcoolicos')
#     print(' 3 - Sair')
#     print('='*50)
# else:
#     print('='*50)
#     print(' 1 - Produtos não alcoolicos')
#     print(' 2 - Sair')
#     print('='*50)


#--- Exercicio 3  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um funcionário
#--- Funcionário: Nome Completo, CPF, Número do registro, Cargo e Salário
#--- Exiba os dados de salário liquido, descontando os tributos
#--- Deve ser calculado o valor do INSS -
#--- INSS -  de    0,00 ate 1751,81 - percetual =  8,0%
#---         de 1751,82 ate 2919,72 - percetual =  9,5%
#---         de 2919,72 ate 5839,45 - percetual = 11,0%
#--- Deve ser calculado o valor do IRRF - 
#--- IRRF -  de    0,00 ate 1903,98 - percetual =  0,0%
#---         de 1903,98 ate 2826,65 - percetual =  7,5%
#---         de 2826,66 ate 3751,05 - percetual = 15,0%
#---         de 3751,06 ate 4664,68 - percetual = 22,5%
#---         de 4664,69 ate ------- - percetual = 27,5%
#--- Base - http://www.calculador.com.br/calculo/salario-liquido

# nome = input('Digite o nome')
# CPF = input('Informe o CPF')
# NR = input('Informe o número de registo')
# cargo = input('Informe o cargo')
# salario = float(input('Qual o salario bruto'))

# if salario <1751.81:
#     if salario < 1903.98:
#         INSS = (8*salario)/100
#         IRRF = salario*0
#         print(f'INSS = {INSS}')
#         print(f'IRRF = {IRRF}')
#         print(f'Salario liquido = {salario-INSS-IRRF}')
# if salario >= 1751.81 and  salario < 2919.72:
#     if salario < 1903.98:
#         INSS = (9.5*salario)/100
#         IRRF = salario*0
#         print(f'INSS = {INSS}')
#         print(f'IRRF = {IRRF}')
#         print(f'Salario liquido = {salario-INSS-IRRF}')
#     elif salario >= 1903.98 and salario <2826.65:
#         INSS = (9.5*salario)/100
#         IRRF = (7.5*salario)/100
#         print(f'INSS = {INSS}')
#         print(f'IRRF = {IRRF}')
#         print(f'Salario liquido = {salario-INSS-IRRF}')
#     elif salario >=2826.65 and salario <3751.05:
#         INSS = (9.5*salario)/100
#         IRRF = (15*salario)/100
#         print(f'INSS = {INSS}')
#         print(f'IRRF = {IRRF}')
#         print(f'Salario liquido = {salario-INSS-IRRF}')

# if salario  >=2919.72 and salario< 5839.45:
#     if salario >=2826.66 and 3751.05:
#         INSS = (11*salario)/100
#         IRRF = (15*salario)/100
#         print(f'INSS = {INSS}')
#         print(f'IRRF = {IRRF}')
#         print(f'Salario liquido = {salario-INSS-IRRF}')
#     elif salario >= 3751.45 and salario<=4664.68:
#         INSS = (11*salario)/100
#         IRRF = (22.5*salario)/100
#         print(f'INSS = {INSS}')
#         print(f'IRRF = {IRRF}')
#         print(f'Salario liquido = {salario-INSS-IRRF}')
#     elif salario > 4664.68:
#         INSS = (11*salario)/100
#         IRRF = (27.5*salario)/100
#         print(f'INSS = {INSS}')
#         print(f'IRRF = {IRRF}')
#         print(f'Salario liquido = {salario-INSS-IRRF}')



#--- Exercicio 4  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que realize a autenticação de usuário
#--- Crie duas variáveis para conter o usuário e senha padrão do sistema
#--- Leia o usuário e senha informados pelo usuário via função input()
#--- Valide se usuário e senha estão corretos
#--- Caso o usuário e senha estejam corretos informe com mensagem de boas vindas
#--- Caso o usuário e senha estejam incorretos informe com mensagem de falha de login

# usuario = input('Cadastre o nome de usuario')
# senha = input('Cadastre a senha')

# ler = input('Informe o nome de usuario')
# ler2 = input('Senha')

# if ler == usuario and ler2 == senha:
#     print(f'Seja bem vindo {usuario}')
# else:
#     print('Falha no login')


#--- Exercicio 5  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia o salário de uma pessoa
#--- Use o método 50-20-10-20 - https://www.jaseimevirar.com/blog/como-voce-organiza-seu-orcamento-mensal/
#--- Informe os percentuais e valores que a pessoa deve utilizar em cada categoria
#--- Deve ser utilizado a função format e os caracteres de tabulação e quebra de linha para cada categoria

salario = float(input('Informe seu salario'))

print(f'\n \t Despesas fixas {(50*salario)/100} \n \t Investimentos a longo prazo {(20*salario)/100} \n \t Investimentos a curto prazo {(10*salario)/100} \n \t gastos livres {(20*salario)/100}')
