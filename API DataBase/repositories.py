import pprint

from models import Pessoas
from models import Atividades

# insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome_pessoa='Marcos', idade=30)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela pessoa
def consulta_pessoas():
    lista = Pessoas.query.all()
    nome = Pessoas.query.filter_by(nome_pessoa='Ingrid').first()
    id = Pessoas.query.filter_by(id=1).first()
    print(lista)

# Altera dados na tabela pessoa
def altera_pessoas():
    altera = Pessoas.query.filter_by(nome_pessoa='Paulo').first()
    altera.nome_pessoa = 'Marcos'
    altera.save()

# Exclui dados na tabela pessoa
def exclui_pessoas():
    exclui = Pessoas.query.filter_by(nome_pessoa='Paulo').first()
    exclui.delete()

#insere_pessoas()
#altera_pessoas()
#exclui_pessoas()
#consulta_pessoas()
