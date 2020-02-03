
from flask import Flask
from flask_restful import Api

from Controller.pessoa_controller import PessoaController
from Controller.cargo_controller import CargoController

app = Flask(__name__)
api = Api(app)


api.add_resource(PessoaController, '/api/pessoa', endpoint='pessoas')
api.add_resource(PessoaController, '/api/pessoa/<int:id>', endpoint='pessoa')
api.add_resource(CargoController, '/api/cargo', endpoint='cargos')
api.add_resource(CargoController, '/api/cargo/<int:id>', endpoint='cargo')


@app.route('/')
def inicio():
    return 'Ta funcionando sim'


app.run(debug=True)
