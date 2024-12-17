from util.sql import *

NOME_TABELA = 'Filme'

class FilmeService:
    def criar_filme(c: dict) -> None:
        insert_into_tabela(NOME_TABELA, c)
        
    def read_filmes() -> Optional[list]:
        return select_from_tabela(NOME_TABELA)

    def read_filme(campo: str, valor: str) -> Optional[list]:
        return select_from_tabela_por_condicao(NOME_TABELA, f'WHERE {campo} = \'{valor}\'')
