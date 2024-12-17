from util.sql import *

class CinemaService:
    def criar_cinema(c: dict) -> None:
        insert_into_tabela('Cinema', c)
        
    def read_cinemas() -> Optional[list]:
        return select_from_tabela('Cinema')

    def read_cinema(campo: str, valor: str) -> Optional[list]:
        return select_from_tabela_por_condicao('Cinema', f'{campo} = \'{valor}\'')
