from typing import Optional
from mysql.connector import *


def executar_sql(conexao, sql: str) -> Optional[list]:
    """Executa um sql em uma conexão estabelecida.

    Args:
        conexao (MySQLConnection): A conexão que será utilizada
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
    return executar_sql(f'SELECT * FROM {tabela}')


def insert_into_tabela(d: dict, tabela: str) -> None:
    campos = ', '.join([key for key in d])

    valores = ', '.join('\'' + str(d[key]) + '\'' for key in d)

    sql = f'INSERT INTO {tabela} ({campos}) VALUES ({valores})'

    executar_sql(sql)


if __name__ == "__main__":
    insert_into_tabela({ "nome": "tal", "idade": 3 }, 'tabela')