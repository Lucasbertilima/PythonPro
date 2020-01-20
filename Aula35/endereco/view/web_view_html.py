from flask import Flask,render_template

import sys
sys.path.append('C:/Users/900145/Documents/PythonPro/Aula35/endereco')
from controller.endereco_controller import EnderecoController

app = Flask(__name__)
pc = EnderecoController()

@app.route('/')
def inicio():
    enderecos = pc.listar_todos()
    return render_template('index2.html', lista = enderecos)

app.run()