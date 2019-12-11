dias_mes = {1:31,2:28,3:31,4:31,5:31,6:31,7:31,8:31,9:31,10:31,11:31,12:31,}

mes=int(input('Qual o número do mês?'))
dias=0

print(f'O mês {mes} tem {dias_mes[mes]} dias')

for i in range(mes,13):
    dias += dias_mes[i]
print(f'faltam {dias} dias para o fim do ano')
print(...)