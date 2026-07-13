from database.repository import Repository
from models.usuario import Usuario


class DashboardService:

    def __init__(self):
        self.repo = Repository()

    def obter_usuario(self):

        usuarios = self.repo.listar(Usuario)

        if usuarios:
            return usuarios[0]

        return None