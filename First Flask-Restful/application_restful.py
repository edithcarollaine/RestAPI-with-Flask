from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Desenvolvedor(Resource):

    def get(self):
        return {'nome': 'GET'}

    def put(self):
        return {'nome': 'PUT'}

    def delete(self):
        return {'nome': 'DELETE'}


api.add_resource(Desenvolvedor, '/')

if __name__ == '__main__':
    app.run(debug=True)
