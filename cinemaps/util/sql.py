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


def select_from_tabela_por_condicao(tabela: str, condicao: str) -> Optional[list]:
    conexao = criar_conexao_padrao()
    
    r = executar_sql(conexao, f'SELECT * FROM {tabela} {condicao}')

    fechar_conexao(conexao)
    
    return r


def insert_into_tabela(d: dict, tabela: str) -> None:
    conexao = criar_conexao_padrao()

    campos = ', '.join([key for key in d])

    valores = ', '.join('\'' + str(d[key]) + '\'' for key in d)

    sql = f'INSERT INTO {tabela} ({campos}) VALUES ({valores})'

    executar_sql(conexao, sql)

    fechar_conexao(conexao)


def inserir_cinemas() -> None:
    conexao = criar_conexao_padrao()
    
    cursor = conexao.cursor(dictionary=True)
    
    cursor.execute("USE Cinemaps;")
    
    cursor.execute("DELETE FROM Cinema;")
    
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Moviecom PrudenShopping\", \"Cinema do PrudenShopping, perto da Mara Cakes no piso térreo.\", -22.1157178,-51.4080938, \"\");")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Cinemark Shopping Pátio Higienópolis\", \"Cinema do Shopping Pátio Higienópolis\", -23.5417993, -46.6810528, \"\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Lar Center\", \"Cinema do Lar Center\", -23.521666, -46.6293459, \"https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQsU8cJSvqrTwZzyyKG3NUBlP6Qu7UtL04asMm9z6agBwMU6oSVvBytv3HNy55D7rjCVzK4YzfT2yFzN9kYQezWQzXRuTC8t9KDK-ymH6knClpsaIfwt14thcGoO4fN2KdycVtw_0Y7lRp/s1600/IMG_6597.JPG\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Cinemark Shopping Metrô Santa Cruz\", \"Cinema do Shopping Metrô Santa Cruz, encontrada depois da escada rolante da praça de alimentação, no último andar.\", -23.5989718, -46.637118, \"https://upload.wikimedia.org/wikipedia/commons/d/d9/Cinemark_Metr%C3%B4_Santa_Cruz_-_sagu%C3%A3o_e_auto_atendimento.jpg\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Cinemark Shopping Center Norte\", \"Cinema do Shopping Center Norte, Localizada na escada rolante ao lado do Madero e atrás da Renner.\", -23.521666, -46.6293459, \"https://www.infomoney.com.br/wp-content/uploads/2019/06/cinemark-1.jpg?fit=720%2C480&quality=50&strip=all\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Cinemark Shopping D\", \"Cinema do Shopping D, localizada no Piso G2, em frente aos elevadores.\", -23.521666, -46.6293459, \"https://shoppingd.com.br/wp-content/uploads/2024/06/cine.png\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Cinemark Shopping Metrô Tucuruvi\", \"Cinema do Shopping Metrô Tucuruvi, acessado no piso L5, ao lado do Jhonny Rockets.\", -23.4802294, -46.6032211, \"\")")
    
    conexao.commit()
    
    fechar_conexao(conexao)


def criar_banco_cinemaps() -> None:
    conexao = criar_conexao_padrao()
    
    cursor = conexao.cursor(dictionary=True)

    print("Teste")
    
    cursor.execute(
        """
        CREATE DATABASE IF NOT EXISTS Cinemaps;
        USE Cinemaps;
        
        CREATE TABLE IF NOT EXISTS Cinema (
            id_cinema INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            foto TEXT,
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
