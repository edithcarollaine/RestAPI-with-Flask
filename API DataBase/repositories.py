import pprint

from models import Pessoas
from models import Atividades
from models import Usuarios

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

def consulta_pessoa_atividades():
    consulta = Atividades.query.all()
    print(consulta)

def delete_pessoa_atividade():
    deleta = Atividades.query.filter_by(nome_atividade='Desenvolver front end do sistema web com python e Django').first()
    deleta.delete()

def insere_usuario():
    inserido = Usuarios(login='ingrid', senha='456')
    inserido.save()

def consulta_all_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)




if __name__ == '__main__':


    #insere_usuario()
    consulta_all_usuarios()
    # insere_pessoas()
    # altera_pessoas()
    # exclui_pessoas()
    # consulta_pessoas()
    # delete_pessoa_atividade()
    # consulta_pessoa_atividades()
