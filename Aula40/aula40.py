from flask import Flask
from flask_restful import Api
import sys
sys.path.append('C:/Users/900145/Documents/PythonPro/Aula40')
from Controller.cerveja_controller import CervejaController


app = Flask(__name__)
api = Api(app)
api.add_resource(CervejaController,'/api/cerveja')
@app.route('/')
def inicio():
    return 'abcdefghijklmnopqrstuvwxyz'

app.run(debug=True)