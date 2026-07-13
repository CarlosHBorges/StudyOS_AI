from sqlalchemy import Column, Integer, String

from database.database import Base


class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String)

    objetivo = Column(String)

    cargo = Column(String)

    empresa = Column(String)

    horas_estudadas = Column(Integer, default=0)