from mysql.connector import *
from .sql import *


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


def criar_conexao_padrao() -> None:
    return abrir_conexao('localhost', 'estudante1', '123', 123, 'Cinemaps')


def criar_banco_cinemaps() -> None:
    executar_sql(
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
            email VARCHAR(100) NOT NULL UNIQUE,
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