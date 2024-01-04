from flask_restful import Resource

lista_habilidade = ['Python', 'Java', 'React', 'Flask', 'PHP']
class Habilidades(Resource):
    def get(self):
        return lista_habilidade