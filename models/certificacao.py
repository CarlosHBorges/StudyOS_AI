from sqlalchemy import Column, Integer, String

from database.database import Base


class Certificacao(Base):

    __tablename__ = "certificacoes"

    id = Column(Integer, primary_key=True)

    nome = Column(String)

    progresso = Column(Integer)

    status = Column(String)