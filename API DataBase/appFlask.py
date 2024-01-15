import json

from flask import Flask
from flask import request

from flask_restful import Resource
from flask_restful import Api
from sqlalchemy.orm import joinedload

from models import Pessoas
from models import Atividades

app = Flask(__name__)
api = Api(app)


class PessoasAPI(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome_pessoa=nome).first()
        try:
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome_pessoa,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                'status': 'Error',
                'mensagem': 'Pessoa não encontrada'
            }
        return response

    def put(self, nome):
        alterar = Pessoas.query.filter_by(nome_pessoa=nome).first()
        if alterar:
            dados = json.loads(request.data)

            if 'nome' in dados:
                alterar.nome_pessoa = dados['nome']

            if 'idade' in dados:
                alterar.idade = dados['idade']

            alterar.save()

            response = {
                'id': alterar.id,
                'nome': alterar.nome_pessoa,
                'idade': alterar.idade
            }

            return response
        else:
            return {'mensagem': 'Pessoa nao encontrada'}, 404


    def delete(self, nome):
        remove = Pessoas.query.filter_by(nome_pessoa=nome).first()
        remove.delete()

        return {f'status': 'sucesso!', 'mensagem': 'Pessoa removida.'}


class ListaPessoasAPI(Resource):

    def get(self):
        lista = Pessoas.query.all()
        response = [{'id': result.id, 'nome': result.nome_pessoa, 'idade': result.idade} for result in lista]
        return response

    def post(self):
        dados = json.loads(request.data)
        verifica = Pessoas.query.filter_by(nome_pessoa=dados['nome']).first()  # Filtra pelo nome para saber se possui o mesmo nome no banco de dados

        # Se retornar verdadeiro, ele não adiciona o nome ao banco de dados e retorna o erro
        if verifica:
            return {'status': 'Error', 'mensagem': 'Nome ja existe no DataBase'}

        # Se retornar false, adiciona o nome ao banco de dados
        else:
            adicionar = Pessoas(nome_pessoa=dados['nome'], idade=dados['idade'])

            adicionar.save()

            response = {
                'id': adicionar.id,
                'nome': adicionar.nome_pessoa,
                'idade': adicionar.idade
            }

        return response, 201


class ListaAtividadeAPI(Resource):

    def get(self):
        lista = Atividades.query.all()
        try:
            response = [{'id': atividade.id, 'pessoa': atividade.pessoa.nome_pessoa if atividade.pessoa is not None else None, 'atividades': atividade.nome_atividade} for atividade in lista]
        except Exception as e:
            print(f"Erro ao encontrar pessoa: {e}")
            return {'status': 'Error', 'mensagem': 'Erro ao encontrar pessoa'}, 500

        return response

    def post(self):
        dados = json.loads(request.data)
        # verifica se o nome está no banco de dados
        pessoa = Pessoas.query.filter_by(nome_pessoa=dados['pessoa']).first()

        if pessoa is None:
            # Se a pessoa não existir, crie uma nova
            pessoa = Pessoas(nome_pessoa=dados['pessoa'])

        if pessoa is not None:
            adicionar_atividade = Atividades(nome_atividade=dados['atividade'], pessoa=pessoa)

            try:
                adicionar_atividade.save()
            except Exception as e:
                print(f"Erro ao salvar atividade: {e}")
                return {'status': 'Error', 'mensagem': 'Erro ao salvar a atividade'}, 500

            response = {
                'id': adicionar_atividade.id,
                'pessoa': adicionar_atividade.pessoa.nome_pessoa,
                'atividade': adicionar_atividade.nome_atividade
            }

            return response
        else:
            return {'status': 'Error', 'mensagem': 'Pessoa não encontrada no banco de dados'}, 404

class AtividadesAPI(Resource):

    def get(self, pessoa):
        buscar = Pessoas.query.filter_by(nome_pessoa=pessoa).first()

        try:
            atividades = [{'id': atividade.id, 'pessoa': atividade.pessoa.nome_pessoa, 'atividades': atividade.nome_atividade} for atividade in
                          buscar.atividade]
        except Exception as e:
            print(f"Erro ao encontrar pessoa: {e}")
            return {'status': 'Error', 'mensagem': 'Erro ao encontrar pessoa'}, 500

        return atividades


    def delete(self, pessoa):
        # Verifica se a pessoa está no database
        pessoa = Pessoas.query.filter_by(nome_pessoa=pessoa).first()
        if not pessoa:
            return {'status': 'Error', 'mensagem': 'Pessoa não encontrada'}, 404

        # Verifica qual atividade está relacionada a pessoa
        atividade = Atividades.query.filter_by(pessoa_id=pessoa.id).first()


        # Deleta atividade e identifica o erro caso não tenha conseguido deletar
        if atividade:
            try:
                pessoa.delete()
                atividade.delete()
                return {f'status': 'sucesso!', 'mensagem': 'Atividade de pessoa removida.'}
            except Exception as e:
                print(f"Erro ao salvar atividade: {e}")
                return {'status': 'Error', 'mensagem': 'Erro ao salvar a atividade'}, 500
        else:
            return {'status': 'Error', 'mensagem': 'Atividade não encontrada para esta pessoa'}, 404


    def put(self, pessoa):
        alterar = Atividades.query.filter(Atividades.pessoa.has(nome_pessoa=pessoa)).first()

        if alterar:
            dados = json.loads(request.data)

            if 'pessoa' in dados:
                novo_nome_pessoa = dados['pessoa']
                if alterar.pessoa.nome_pessoa != novo_nome_pessoa:
                    pessoa_existente = Pessoas.query.filter_by(nome_pessoa=novo_nome_pessoa).first()
                    if not pessoa_existente:
                        alterar.pessoa.nome_pessoa = novo_nome_pessoa
            if 'atividade' in dados:
                alterar.nome_atividade = dados['atividade']

            alterar.save()

            response = {
                'id': alterar.id,
                'pessoa': alterar.pessoa.nome_pessoa,
                'atividade': alterar.nome_atividade
            }

            return response
        else:
            return {'mensagem': 'Pessoa nao encontrada'}, 404


# ROTAS
api.add_resource(PessoasAPI, '/pessoa/<string:nome>')
api.add_resource(ListaPessoasAPI, '/pessoa')
api.add_resource(ListaAtividadeAPI, '/atividades')
api.add_resource(AtividadesAPI, '/atividades/<string:pessoa>')


if __name__ == '__main__':
    app.run(debug=True)
