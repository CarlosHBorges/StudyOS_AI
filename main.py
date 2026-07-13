from database.database import Base, engine

import models.usuario
import models.trilha
import models.projeto
import models.certificacao

print(Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)