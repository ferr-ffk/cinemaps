from typing import Optional
from .db import criar_conexao_padrao, fechar_conexao


def executar_sql(conexao, sql: str) -> Optional[list]:
    """Executa um sql em uma conexão estabelecida.

    Args:
        conexao (): A conexão que será utilizada
        sql (str): A string do SQL a ser executado
    """

    cursor = conexao.cursor(dictionary=True)
    cursor.execute(sql)

    resultado = []

    for registro in cursor:
        resultado.append(registro)

    conexao.commit()

    return resultado


def select_from_tabela(tabela: str) -> Optional[list]:
    conexao = criar_conexao_padrao()
    
    r = executar_sql(conexao, f'SELECT * FROM {tabela}')

    fechar_conexao(conexao)
    
    return r


def insert_into_tabela(d: dict, tabela: str) -> None:
    conexao = criar_conexao_padrao()

    campos = ', '.join([key for key in d])

    valores = ', '.join('\'' + str(d[key]) + '\'' for key in d)

    sql = f'INSERT INTO {tabela} ({campos}) VALUES ({valores})'

    executar_sql(conexao, sql)

    fechar_conexao(conexao)


if __name__ == "__main__":
    insert_into_tabela({ "nome": "tal", "idade": 3 }, 'tabela')
