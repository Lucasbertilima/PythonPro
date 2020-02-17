from flask import Flask
from flask_restful import Api

from exercicio.controller.reacao_comentario_controller import Reacao_Comentario_Controller
from exercicio.controller.reacao_controller import Reacao_Controller
from exercicio.controller.reacao_post_controller import Reacao_Post_Controller


app = Flask(__name__)
api = Api(app)

api.add_resource(Reacao_Comentario_Controller, '/api/reacao_comentario', endpoint='reacao_c')
api.add_resource(Reacao_Post_Controller, '/api/reacao_post', endpoint='reacao_p')
api.add_resource(Reacao_Controller, '/api/reacao', endpoint='reacao')

app.run(debug=True)