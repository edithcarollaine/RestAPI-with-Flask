import json
from habilidades import Habilidades
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
     'id': '0',
     'nome': 'Rafael',
     'habilidades': ['Python', 'Django']
     },

    {
     'id': '1',
     'nome': 'Ingrid',
     'habilidades': ['Python', 'Flask']
     }
]

#  retorna um desenvolvedor pelo ID, altera e deleta
class Desenvolvedor(Resource):

    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} nao existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluído!'}


# lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return (desenvolvedores[posicao])


api.add_resource(Desenvolvedor, '/<int:id>')
api.add_resource(ListaDesenvolvedores, '/lista')
api.add_resource(Habilidades, '/habilidades')


if __name__ == '__main__':
    app.run()
