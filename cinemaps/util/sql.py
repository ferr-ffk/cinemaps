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


def select_from_tabela_por_id(tabela: str, id: int) -> Optional[list]:
    conexao = criar_conexao_padrao()
    
    r = executar_sql(conexao, f'SELECT * FROM {tabela} WHERE id = {id}')

    fechar_conexao(conexao)
    
    return r


def insert_into_tabela(d: dict, tabela: str) -> None:
    conexao = criar_conexao_padrao()

    campos = ', '.join([key for key in d])

    valores = ', '.join('\'' + str(d[key]) + '\'' for key in d)

    sql = f'INSERT INTO {tabela} ({campos}) VALUES ({valores})'

    executar_sql(conexao, sql)

    fechar_conexao(conexao)


def criar_banco_cinemaps() -> None:
    conexao = criar_conexao_padrao()
    
    cursor = conexao.cursor(dictionary=True)
    
    cursor.execute(
        """
        CREATE DATABASE IF NOT EXISTS Cinemaps;
        USE Cinemaps;



        CREATE TABLE IF NOT EXISTS Cinema (
            id_cinema INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            fonte TEXT,
            descricao TEXT,
            latitude DECIMAL(9,6) NOT NULL,
            longitude DECIMAL(9,6) NOT NULL
        );


        CREATE TABLE IF NOT EXISTS Genero (
            id_genero INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Filme (
            id_filme INT AUTO_INCREMENT PRIMARY KEY,
            descricao TEXT,
            titulo VARCHAR(100) NOT NULL,
            duracao TIME NOT NULL,
            id_genero INT NOT NULL,
            FOREIGN KEY (id_genero) REFERENCES Genero(id_genero)
        );



        CREATE TABLE IF NOT EXISTS Usuario (
            id_usuario INT AUTO_INCREMENT PRIMARY KEY,
            usuario VARCHAR(100) NOT NULL UNIQUE,
            email VARCHAR(100) NOT NULL,
            apelido VARCHAR(50),
            senha VARCHAR(255) NOT NULL
        );


        CREATE TABLE IF NOT EXISTS Sessao (
            id_sessao INT AUTO_INCREMENT PRIMARY KEY,
            id_cinema INT NOT NULL,
            id_filme INT NOT NULL,
            data_horario DATETIME NOT NULL,
            ativa BOOLEAN DEFAULT TRUE,
            FOREIGN KEY (id_cinema) REFERENCES Cinema(id_cinema),
            FOREIGN KEY (id_filme) REFERENCES Filme(id_filme)
        );


        CREATE TABLE IF NOT EXISTS Avaliacao (
            id_avaliacao INT AUTO_INCREMENT PRIMARY KEY,
            nota INT NOT NULL CHECK (nota BETWEEN 1 AND 5),
            numero_avaliacoes INT DEFAULT 1,
            descricao TEXT,
            id_cinema INT NOT NULL,
            id_usuario INT NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
            FOREIGN KEY (id_cinema) REFERENCES Cinema(id_cinema)
        );


        CREATE TABLE IF NOT EXISTS Favorito (
            id_usuario INT NOT NULL,
            id_cinema INT NOT NULL,
            PRIMARY KEY (id_usuario, id_cinema),
            FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
            FOREIGN KEY (id_cinema) REFERENCES Cinema(id_cinema)
        );
        """)
    
    fechar_conexao(conexao)


if __name__ == "__main__":
    insert_into_tabela({ "nome": "tal", "idade": 3 }, 'tabela')
