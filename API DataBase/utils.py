from sqlalchemy import update
from sqlalchemy import insert
from sqlalchemy import delete

from models import User
from models import Exercicio
from models import session

print('\nBUSCA FILTRADA')
busca_um = session.query(User).filter_by(nome_pessoa='edith')
for result in busca_um:
    print(result)
busca_dois = session.query(Exercicio).filter_by(id=1)
for result in busca_dois:
    print(result)

print('\nLISTA ORDENADA DO USER')
mostrar = session.query(User).order_by()
for result in mostrar:
    print(result)

print('\nLISTA ORDENADA DOS EXERCICIOS')
mostrar = session.query(Exercicio).order_by()
for result in mostrar:
    print(result)

print('\nUPDATE EM USER')
alterar = session.execute(update(User).where(User.id.in_([3])).values(idade=30))
busca_dois = session.query(User).filter_by(id=3)
for result in busca_dois:
    print(result)

print('\nINSERT EM USER')
inserir_um = session.execute(insert(User).values(nome_pessoa='joao', idade=18))
inserir_dois = session.execute(insert(User).values(nome_pessoa='felipe', idade=50))
print('Valores inseridos com sucesso!')

print('\nMOSTRANDO VALORES ATUALIZADOS')
mostrar = session.query(User).order_by()
for result in mostrar:
    print(result)

print('\nDELETE EM USER')
delete = session.execute(delete(User).where(User.id.in_([5, 6])))
print('Valores deletados com sucesso!')

print('\nMOSTRANDO VALORES ATUALIZADOS')
mostrar = session.query(User).order_by()
for result in mostrar:
    print(result)


