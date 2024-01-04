from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)


@app.route('/<int:id>')
def pessoas(id):
    return jsonify({'id': 1,
                    'nome': 'Rafael',
                    'idade': 15,
                    'profissao': 'Desenvolvedor'})

@app.route('/soma', methods=['POST','GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
        return jsonify({'soma': total})

    elif request.method == 'GET':
        total = 10 + 10

    return jsonify(({'soma': total}))

if __name__ == '__main__':
    app.run(debug=True)
