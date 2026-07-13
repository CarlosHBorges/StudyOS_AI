from sqlalchemy import Column, Integer, String

from database.database import Base


class Projeto(Base):

    __tablename__ = "projetos"

    id = Column(Integer, primary_key=True)

    nome = Column(String)

    progresso = Column(Integer)

    status = Column(String)

    prioridade = Column(String)