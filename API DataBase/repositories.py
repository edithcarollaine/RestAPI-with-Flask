import pprint

from models import Pessoas

# insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome_pessoa='Paulo', idade=20)
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


if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoas()
    exclui_pessoas()
    consulta_pessoas()
