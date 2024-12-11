from util.sql import *

class UsuarioService:
    def criar_usuario(u: dict) -> None:
        insert_into_tabela(u, 'Usuario')

    def read_usuarios() -> Optional[list]:
        return select_from_tabela('Usuario')
