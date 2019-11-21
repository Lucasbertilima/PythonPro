#--- 2-Crie um programa que calcule a rentabiblidade anual de um investimento 
#---   baseando-se em sua rentabilidade mensal(juros compostos) 
#---   a rentabilidade deve ser apresentada em % e R$ utilizar metodos
from metodos import rentabiblidade

val= float(input('Qual o valor do investimento?'))
juros1=float(input('Qual a porcentagem dos juros ao mês?'))

valort = rentabiblidade(val,juros1)

print(f'A o valor total é {valort} \n')


# valanual = rentabiblidade(val,juros1)
# print(valanual)