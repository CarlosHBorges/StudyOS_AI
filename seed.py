from database.repository import Repository

from models.usuario import Usuario

repo = Repository()

usuarios = repo.listar(Usuario)

if len(usuarios) == 0:

    usuario = Usuario(
        nome="Carlos Henrique",
        objetivo="Engenheiro de Dados",
        cargo="Analista de Dados",
        empresa="StudyOS AI",
        horas_estudadas=128
    )

    repo.salvar(usuario)

    print("Usuário criado!")

else:

    print("Usuário já existe.")