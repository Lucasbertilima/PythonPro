# Aula 9 - 19-11-2019
#--- def

from metodos import calculo_inss,calculo_irrf

salario = float(input('Qual o salario bruto'))
inss = calculo_inss(salario)
irrf = calculo_irrf(salario,inss)


print (f'Inss: {inss}')
print (f'Irrf: {irrf}')
print (f'salario liquido = {salario-inss-irrf}')
