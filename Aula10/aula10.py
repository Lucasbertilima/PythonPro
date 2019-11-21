# Aula 10 - 20-11-2019
#
#--- Web - Calculador

nome = 'Calculadora'
from flask import Flask,render_template,request
from metodos import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',titulo=nome)
@app.route('/calcular')
def calcular():
    n1 =int(request.args['n1'])
    n2 =int(request.args['n2'])
    
    som = soma(n1,n2)
    subtr = subtracao(n1,n2)
    mult = multiplicacao(n1,n2)
    divint = div_int(n1,n2)
    divif = divisaof(n1,n2)
    restdiv = restodiv(n1,n2)
    raiz1 = raiz(n1,n2)
    pot = potencia(n1,n2)
    resultados= {'som':som,'subtr':subtr,'mult':mult,'divint':divint,'divif':divif,'restdiv':restdiv,'raiz1':raiz1,'pot':pot}
    return render_template('resultado.html',n1 =n1,n2=n2,resultados=resultados)
app.run(debug=True)