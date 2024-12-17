from util.sql import *

class UsuarioService:
    def criar_usuario(u: dict) -> None:
        insert_into_tabela(u, 'Usuario')

    def read_usuarios() -> Optional[list]:
        return select_from_tabela('Usuario')
    
    def read_usuario(campo: str, valor: str) -> Optional[list]:
        return select_from_tabela_por_condicao('Usuario', f'{campo} = \'{valor}\'')
