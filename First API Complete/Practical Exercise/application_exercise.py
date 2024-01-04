'''
Rest API gerenciador de cadastro de tarefas
'''

from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)
lista_tarefas = [
    {
        'id': '0',
        'responsavel': 'Edith',
        'tarefas': ['Arrumar a casa',
                    'lavar o banheiro',
                    'fazer o almoco'],
        'status': 'concluido'

    },
    {
        'id': '1',
        'responsavel': 'Marcos',
        'tarefas': ['passar roupa',
                    'lavar a area,'
                    'fazer o jantar'],
        'status': 'pendente'

    }
]

# Retornando a lista_tarefa e também adicionando novas tarefas
@app.route('/lista/', methods = ['GET', 'POST'])
def tarefas():
# Retornando a lista_tarefa
    if request.method == 'GET':
        return jsonify(lista_tarefas)

# Adiciona um nova tarefa a lista_tarefa
    elif request.method == 'POST':
        result = json.loads(request.data)
        position = len(lista_tarefas)
        result['id'] = position
        lista_tarefas.append(result)

        return jsonify(lista_tarefas[position])


@app.route('/lista/<int:id>/', methods=['GET', 'PUT'])
def alterar_campos(id):
# Consultar tarefa através do ID
    if request.method == 'GET':
        try:
            response = lista_tarefas[id]
        except IndexError:
            mensagem = f'Nao existe tarefa com este ID: {id}'
            response = {'Informacao': 'Erro!', 'mensagem': mensagem}

        except Exception:
            mensagem = f'Erro desconhecido. Por favor procure o administrador da API'
            response = {'Informacao': 'Erro!', 'mensagem': mensagem}

        return jsonify(response)

# Alterar status (FALTANDO AINDA)
    if request.method == 'PUT':
        result = json.loads(request.data)  # faz a leitura dos dados em json
        lista_tarefas[id] = result  # chama a tarefa pelo ID

        return jsonify(result)  # retorna com os dados alterados

# Deleta a tarefa
@app.route('/lista/<int:id>/', methods=['DELETE'])
def delete_tarefa():
    lista_tarefas.pop(id)
    return jsonify({'Informacao': 'Sucesso!', 'mensagem': 'A tarefa foi excluida'})

if __name__ == '__main__':
    app.run()
