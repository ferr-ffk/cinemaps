from mysql.connector import connect, MySQLConnection


def abrir_conexao(host: str, usuario: str, senha: str, banco: str) -> MySQLConnection:
    """Abre uma conexão MySQL e retorna ela

    Args:
        host (str): O valor para o host da sessão
        usuario (str): O nome de usuário para acessar o banco
        senha (str): A senha do usuário
        banco (str): O nome do banco de dados

    Returns:
        MySQLConnection: A conexão estabelecida
    """

    return connect(host=host, user=usuario, password=senha, database=banco)

def fechar_conexao(con: MySQLConnection) -> None:
    """Fecha a conexão.

    Args:
        con (MySQLConnection): A conexão a ser fechada
    """

    con.close()


def criar_conexao_padrao() -> MySQLConnection:
    return abrir_conexao('localhost', 'estudante1', '123456', 'Cinemaps')
