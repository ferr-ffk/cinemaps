from util.sql import *

NOME_TABELA = 'Sessao'

class SessaoService:
    def criar_sessao(c: dict) -> None:
        insert_into_tabela(NOME_TABELA, c)
        
    def read_sessoes() -> Optional[list]:
        return select_from_tabela(NOME_TABELA)

    def read_sessao(campo: str, valor: str) -> Optional[list]:
        return select_from_tabela_por_condicao(NOME_TABELA, f'WHERE {campo} = \'{valor}\'')
