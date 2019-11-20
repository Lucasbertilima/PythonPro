def calculo_inss(salario):
    if salario <1751.81:
        inss = salario*0.08
        print(f'salario - inss {salario-inss}')
    if salario >= 1751.81 and  salario < 2919.72:
        inss = salario*0.95
        print(f'salario - inss {salario-inss}')
    if salario  >=2919.72 and salario< 5839.45:
        inss = salario*0.11
        print(f'salario - inss {salario-inss}')
    else:
        inss = 642.34

    return inss

def calculo_irrf(salario,inss):
    if salario>=0 and salario<=1903.98:
        irrf=(salario-inss) * 0
    elif salario>1903.98 and salario<=2826.65:
        irrf=(salario-inss) * 0.075
    elif salario>2826.65 and salario <=3751.05:
        irrf=(salario-inss) * 0.15
    elif salario >3751.05 and salario<=4663.68:
        irrf=(salario-inss) * 0.225
    elif (salario >4663.68):
        irrf=(salario-inss) * 0.275
    return irrf

def soma(n1,n2):
    som = n1+n2
    return som
def subtracao(n1,n2):
    subtr = n1-n2
    return subtr
def multiplicacao(n1,n2):
    mult= n1*n2
    return mult

def div_int(n1,n2):
    divint = n1//n2
    return divint

def divisaof(n1,n2):
    divif = n1/n2
    return divif

def restodiv(n1,n2):
    restdiv = n1%n2
    return restdiv

def raiz(n1,n2):
    raiz1 = n1 **(1/n2)
    return raiz1

def potencia(n1,n2):
    pot=n1**n2
    return pot
