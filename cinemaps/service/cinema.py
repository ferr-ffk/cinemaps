from util.sql import *

class CinemaService:
    def criar_cinema(c: dict) -> None:
        insert_into_tabela('cinema', c)
        
    def read_cinemas() -> Optional[list]:
        return select_from_tabela('cinema')