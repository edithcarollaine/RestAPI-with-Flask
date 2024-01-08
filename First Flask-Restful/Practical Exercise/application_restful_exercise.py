import json
from flask import request, Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

lista_habilidade = ['Python', 'Java', 'React', 'Flask', 'PHP']

# Pelo ID: busca, altera e deleta
class Habilidades(Resource):
    def get(self, id):
        try:
            response = lista_habilidade[id]
        except IndexError:
            mensagem = f'Habilidade de ID {id} nao existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):

        dados = json.loads(request.data)
        lista_habilidade[id] = dados
        return dados

    def delete(self, id):

        lista_habilidade.pop(id)
        return {'status': 'sucesso', 'mensagem': 'habilidade excluída!'}

# Lista todas as habilidades e adiciona uma nova
class ListaHabilidades(Resource):
    def get(self):
        return lista_habilidade

    def post(self):
        dados = json.loads(request.data)
        lista_habilidade.append(dados)
        return lista_habilidade

api.add_resource(ListaHabilidades, '/habilidades')
api.add_resource(Habilidades, '/habilidades/<int:id>')

if __name__ == '__main__':
    app.run()
