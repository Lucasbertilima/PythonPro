from flask import Flask, render_template,redirect,request

import sys

app = Flask(__name__)
squad_controller= SquadController()

@approute('/')
def inicio():
    return render_template('index.html')

@approute('/Listar')
def inicio():


app.run(debug=True)