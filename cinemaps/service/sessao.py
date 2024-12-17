from util.sql import *

NOME_TABELA = 'Sessao'

class SessaoService:
    def criar_sessao(c: dict) -> None:
        insert_into_tabela(NOME_TABELA, c)
        
    def read_sessoes() -> Optional[list]:
        conexao = criar_conexao_padrao()

        r = executar_sql(conexao, f'SELECT *, DATE_FORMAT(data_horario, \'%d/%m/%y às %H:%i\') as format_data_horario from {NOME_TABELA}')
    
        fechar_conexao(conexao)

        return r

    def read_sessoes_por_condicao(campo: str, valor: str) -> Optional[list]:
        conexao = criar_conexao_padrao()

        r = executar_sql(conexao, f'SELECT *, DATE_FORMAT(data_horario, \'%d/%m/%y às %H:%i\') as format_data_horario from {NOME_TABELA} WHERE {campo} = \'{valor}\'')
    
        fechar_conexao(conexao)

        return r
