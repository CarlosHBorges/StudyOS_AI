from database.database import SessionLocal


class Repository:

    def __init__(self):

        self.db = SessionLocal()

    def salvar(self, objeto):

        self.db.add(objeto)

        self.db.commit()

        self.db.refresh(objeto)

        return objeto

    def listar(self, model):

        return self.db.query(model).all()