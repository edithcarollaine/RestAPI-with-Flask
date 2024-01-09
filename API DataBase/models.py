from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # attributes
    id = Column(Integer, primary_key=True)
    nome_pessoa = Column(String, index=True)
    idade = Column(Integer)

    exercicio = relationship('Exercicio', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f'Usuário(id={self.id}, nome = {self.nome_pessoa}, idade={self.idade})'


class Exercicio(Base):
    __tablename__ = 'exercicio'
    #attributes
    id = Column(Integer, primary_key=True)
    nome_exercicio = Column(String(100))
    pessoa_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship('User', back_populates='exercicio')

    def __repr__(self):
        return f'Exercicio(id={self.id}, nome_exercicio={self.nome_exercicio})'


engine = create_engine('sqlite://')
Base.metadata.create_all(engine)

# inserção de valores ao banco INSERT
with Session(engine) as session:
    pessoa_um = User(
        nome_pessoa='edith',
        idade=26,
        exercicio=[Exercicio(nome_exercicio='Flexoes')],
    )
    pessoa_dois = User(
        nome_pessoa='ingrid',
        idade=19,
        exercicio=[Exercicio(nome_exercicio='Abdominais')]
    )
    pessoa_tres = User(
        nome_pessoa='paulo',
        idade=23,
        exercicio=[Exercicio(nome_exercicio='Corridas de 2km')],
    )
    pessoa_quatro = User(
        nome_pessoa='rafael',
        idade=29,
        exercicio=[Exercicio(nome_exercicio='Corridas de 1km')],
    )


    # send of database
    # enviando para o banco de dados (persistência de dados)

'''Só usa se tiver certeza da persistência dos dados'''
session.add_all([pessoa_um, pessoa_dois, pessoa_tres, pessoa_quatro])
session.commit()


