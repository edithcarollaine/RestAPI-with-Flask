from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


engine = create_engine('sqlite:///database.db')
db_session = scoped_session(sessionmaker(autoflush=False, autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True)
    nome_pessoa = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return f'\nPessoa com nome: {self.nome_pessoa} e idade: {self.idade}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ = 'atividades'

    id = Column(Integer, primary_key=True)
    nome_atividade = Column(String(100), index=True)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas')

    def __repr__(self):
        return f'\nPAtividade: {self.nome_atividade}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()