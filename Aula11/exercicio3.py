#--- 3- Crie um programa para calculo de investimento
#---    Solicitar a quantidade de cotas no Tesouro selic(minima 0.01)
#---    (Considerar valor do tesouro Selic Hoje) 10410.00 min 104.10
#---    Calcular o valor total até o vencimento do titulo  01/03/2025
#---    Utilizar metodos
from metodos2 import selic
q=float(input('Quantas cotas deseja comprar? minimo 0.01'))
selic=selic(q)

print (selic)