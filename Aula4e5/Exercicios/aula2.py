#--- Exercicio 1  - Variávies e impressão com interpolacão de string
#--- Crie 5 variávies para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Os dados devem ser impressos utilizando a funcao format()
#--- Deve ser usado apenas uma vez a função print(), porem os dados devem ser apresentados um em cada linha
#--- O salario deve ser de tipo flutuante e na impressão deve apesentar apenas duas casas após a vírgula

# nome = input('Digite seu nome')
# Sobrenome = input('Digite seu sobrenome')
# CPF = input('Informe o seu CPF')
# RG = input('Informe seu RG')
# salario= float(input('Informe o seu sálario'))

# print(f'O nome é {nome} \n O Sobrenome é {Sobrenome} \n o CPF é {CPF} \n o RG é {RG} \n e o salário é {salario}')

#--- Exercicio 2  - Variávies e impressão com interpolacão de string
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format() para concatenar os números da opções, que devem ser números inteiros
#--- Alem das opções o menu deve conter um cabeçalho e um rodapé
#--- O cabeçalho e o rodapé devem ser impressos utilizando a multiplicação de caracters
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação

# print('='*50,'\n'*3)
# print('O que deseja fazer?')
# print('1 - Logar')
# print('2 - Cadastrar usuario')
# print('3 - Sair ',' \n'*3)
# print('='*50)

#--- Exercicio 3  - Variávies e impressão com interpolacão de string
#--- Imprima dois paragráfos do ultimo livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- Livro: Título, Edição, Autor, Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

# titulo = input ('Digite o titulo do livro')
# edicao = input ('Digite a editora')
# autor  = input('Informe o autor do livro')
# datapu = input('Qual a data de publicação do livro')

# print(f'O Titulo do livro é {titulo} \n editora {edicao} \n autor {autor} \n data de publicação {datapu} ')
# print('Dois paragrafos do livro')
# print('\t Os Grados permaneceram por mais um tempo ao longo das margens do grande rio \n Anduin, e eram reservados em relação aos homens. \n \t Migraranm, para oeste depois dos Pés-peludos e seguiram o curso do \n Ruidoságua em direção ao sul, e ali muitos deles moraram por um longo tempo entre \n Tharbad e os limites da Terra Parda, antes de rumar para o norte novamente.')

#--- Exercicio 4  - Variávies e impressão com interpolacão de string
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- Entre os dois pontos deve conter no minimo 10 pontos de parada
#--- Cada item deve conter data, hora e descrição
#--- O itineário deve conter cabeçalho com o título da viagem
#--- Os dados de cada ponto devem estar em variáveis
#--- Deve ser usado os caracteres de tabulação, quebra de linha e a função Format()

# ppartida = input('Informe o ponto de partida')
# datap = input('Data')
# horap = input('Hora')
# descricaop = input('Descrição do ponto')

# ponto1 = input('Informe o ponto 1')
# data1= input('Data')
# hora1 = input('Hora')
# descricao1 = input('Descrição do ponto')

# ponto2 = input('Informe o ponto 2')
# data2 = input('Data')
# hora2 = input('Hora')
# descricao2 = input('Descrição ')

# ponto3 = input('Informe o ponto 3')
# data3  = input('Data')
# hora3  = input('Hora')
# descricao3 = input('Descrição ')

# ponto4 = input('Informe o ponto 4')
# data4 = input('Data')
# hora4 = input('Hora')
# descricao4 = input('Descrição do ponto')

# ponto5 = input('Informe o ponto 5')
# data5 = input('Data')
# hora5 = input('Hora')
# descricao5 = input('Descrição do ponto')

# ponto6 = input('Informe o ponto 6')
# data6 = input('Data')
# hora6 = input('Hora')
# descricao6 = input('Descrição do ponto')

# ponto7 = input('Informe o ponto 7')
# data7 = input('Data')
# hora7 = input('Hora')
# descricao7 = input('Descrição do ponto')

# ponto8 = input('Informe o ponto 8')
# data8= input('Data')
# hora8 = input('Hora')
# descricao8 = input('Descrição do ponto')

# ponto9 = input('Informe o ponto 9')
# data9 = input('Data')
# hora9 = input('Hora')
# descricao9 = input('Descrição do ponto')

# ponto10 = input('Informe o ponto 10')
# data10 = input('Data')
# hora10 = input('Hora')
# descricao10 = input('Descrição do ponto')

# pfinal = input('Informe o ponto final')
# dataf = input('Data')
# horaf = input('Hora')
# descricaof = input('Descrição do ponto')

# titulo = input('Informe o titulo da viagem')

# print('='*50,f'\n \t {titulo}\t  \n ponto de partida {ppartida} data {datap} horario {horap}')
# print(f'ponto 1 {ponto1} data {data1} horario {hora1}')
# print(f'ponto 2 {ponto2} data {data2} horario {hora2}')
# print(f'ponto 3 {ponto3} data {data3} horario {hora3}')
# print(f'ponto 4 {ponto4} data {data4} horario {hora4}')
# print(f'ponto 5 {ponto5} data {data5} horario {hora5}')
# print(f'ponto 6 {ponto6} data {data6} horario {hora6}')
# print(f'ponto 7 {ponto7} data {data7} horario {hora7}')
# print(f'ponto 8 {ponto8} data {data8} horario {hora8}')
# print(f'ponto 9 {ponto9} data {data9} horario {hora9}')
# print(f'ponto 10 {ponto10} data {data9} horario {hora10}')
# print(f'ponto final {pfinal} data {dataf} horario {horaf}')
# print('='*50)

#--- Exercicio 5  - Variávies e impressão com interpolacão de string
#--- Imprima os dados de 5 papeis cotatos na bolsa de valors de SP
#--- Os dados dos papeis devem estar em variáveis
#--- Papel: Nome, Tipo, Cotação Atual e Valores Min e Max do dia 
#--- A tela deve conter cabeçalho e rodapé 

