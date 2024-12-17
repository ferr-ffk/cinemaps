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


def inserir_sessoes_filmes() -> None:
    conexao = criar_conexao_padrao()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("USE Cinemaps;")

    cursor.execute("INSERT INTO Genero (nome) VALUES (\"Terror\");")
    cursor.execute("INSERT INTO Genero (nome) VALUES (\"Live Action\");")

    conexao.commit()

    cursor.execute("INSERT INTO Filme (descricao, titulo, duracao, id_genero, foto) VALUES (\"Um homem, desesperado por dinheiro para ajudar a sua irmã, aceita uma vaga de emprego de segurança noturno em uma antiga pizzaria, mas mal sabe ele a história por trás de de tal pizzaria e o que o aguarda\", \"Five Nights at Freddy: O Pesadelo sem Fim\", \"01:50:00\", 1, \"https://www.universalpics.com.br/tl_files/content/movies/five_nights/posters/07.jpg\");")
    cursor.execute("INSERT INTO Filme (descricao, titulo, duracao, id_genero, foto) VALUES (\"Quatro jogadores vão parar em um mundo místico, onde um veterano os ensina o básico para sobrevivência nesse mundo\", \"Minecraft: Um Filme\", \"01:53:40\", 2, \"https://pt.minecraft.wiki/images/thumb/A_Minecraft_Movie_Teaser_Poster.jpg/300px-A_Minecraft_Movie_Teaser_Poster.jpg?9e74d\");")

    conexao.commit()

    # cursor.execute("USE Cinemaps;")

    # conexao.commit()

    fechar_conexao(conexao)

    inserir_sessoes()


def inserir_sessoes() -> None:
    conexao = criar_conexao_padrao()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("USE Cinemaps;")
    
    cursor.execute("INSERT INTO `Sessao` (id_cinema, id_filme, data_horario) VALUES (1, 2, \"2025-05-25 14:55:00\");")
    cursor.execute("INSERT INTO `Sessao` (id_cinema, id_filme, data_horario) VALUES (2, 1, \"2025-04-29 17:50:00\");")
    cursor.execute("INSERT INTO `Sessao` (id_cinema, id_filme, data_horario) VALUES (3, 2, \"2025-01-17 16:30:00\");")
    cursor.execute("INSERT INTO `Sessao` (id_cinema, id_filme, data_horario) VALUES (5, 2, \"2024-12-29 18:55:00\");")
    cursor.execute("INSERT INTO `Sessao` (id_cinema, id_filme, data_horario) VALUES (4, 1, \"2024-12-22 19:00:00\");")
    cursor.execute("INSERT INTO `Sessao` (id_cinema, id_filme, data_horario) VALUES (7, 2, \"2025-03-30 11:00:00\");")
    cursor.execute("INSERT INTO `Sessao` (id_cinema, id_filme, data_horario) VALUES (6, 2, \"2025-02-23 12:00:00\");")

    conexao.commit()

    fechar_conexao(conexao)


def inserir_cinemas() -> None:
    conexao = criar_conexao_padrao()
    
    cursor = conexao.cursor(dictionary=True)
    
    cursor.execute("USE Cinemaps;")
    
    cursor.execute("DELETE FROM Cinema;")
    
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Moviecom PrudenShopping\", \"Cinema do PrudenShopping, perto da Mara Cakes no piso térreo.\", -22.1157178,-51.4080938, \"https://fastly.4sqi.net/img/general/600x600/QPnQ0Own-cNSgDFewC1fRcrznXfoEUH1WqZp7xi-AsE.jpg\");")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Cinemark Shopping Pátio Higienópolis\", \"Cinema do Shopping Pátio Higienópolis\", -23.5417993, -46.6810528, \"https://www.boletimnerd.com.br/wp-content/uploads/2024/02/semana-do-cinema-shopping-patio-higienopolis.jpg\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Lar Center\", \"Cinema do Lar Center\", -23.521666, -46.6293459, \"https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQsU8cJSvqrTwZzyyKG3NUBlP6Qu7UtL04asMm9z6agBwMU6oSVvBytv3HNy55D7rjCVzK4YzfT2yFzN9kYQezWQzXRuTC8t9KDK-ymH6knClpsaIfwt14thcGoO4fN2KdycVtw_0Y7lRp/s1600/IMG_6597.JPG\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Cinemark Shopping Metrô Santa Cruz\", \"Cinema do Shopping Metrô Santa Cruz, encontrada depois da escada rolante da praça de alimentação, no último andar.\", -23.5989718, -46.637118, \"https://upload.wikimedia.org/wikipedia/commons/d/d9/Cinemark_Metr%C3%B4_Santa_Cruz_-_sagu%C3%A3o_e_auto_atendimento.jpg\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Cinemark Shopping Center Norte\", \"Cinema do Shopping Center Norte, Localizada na escada rolante ao lado do Madero e atrás da Renner.\", -23.521666, -46.6293459, \"https://www.infomoney.com.br/wp-content/uploads/2019/06/cinemark-1.jpg?fit=720%2C480&quality=50&strip=all\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Cinemark Shopping D\", \"Cinema do Shopping D, localizada no Piso G2, em frente aos elevadores.\", -23.521666, -46.6293459, \"https://shoppingd.com.br/wp-content/uploads/2024/06/cine.png\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Cinemark Shopping Metrô Tucuruvi\", \"Cinema do Shopping Metrô Tucuruvi, acessado no piso L5, ao lado do Jhonny Rockets.\", -23.4802294, -46.6032211, \"\")")
    
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"REAG Belas Artes\", \"Complexo de 6 salas de cinema com telas convencionais de tamanho médio que exibem filmes clássicos e de arte.\", -23.555668, -46.6622988, \"https://vault.pulsarimagens.com.br/file/thumb/03EL623.jpg\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"CINESESC\", \"Cinema amplo com filmes nacionais e estrangeiros, poltronas para obesos e comércio de café e doces.\", -23.5604023, -46.6650621, \"https://f.i.uol.com.br/fotografia/2018/03/01/15199395125a986fb82de08_1519939512_3x2_rt.jpg\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Cinemark Shopping Interlagos\", \"Cinema digital e 3D com salas em estilo estádio e VIP, assentos numerados e venda de ingressos on-line.\", -23.6764, -46.6808249, \"https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1d/93/5c/2b/cinemark.jpg?w=900&h=500&s=1\")")
    cursor.execute("INSERT INTO Cinema(nome, descricao, latitude, longitude, foto) VALUES (\"Cinesystem São Paulo Shopping Morumbi Town\", \"Cinema digital e 3D com salas com poltronas grandes VIP, assentos numerados e venda de ingressos on-line.\", -23.6764, -46.6808249, \"https://dynamic-media-cdn.tripadvisor.com/media/photo-o/16/91/94/a0/photo0jpg.jpg?w=900&h=500&s=1\")")
    
    conexao.commit()
    
    fechar_conexao(conexao)


def criar_banco_cinemaps() -> None:
    conexao = criar_conexao_padrao()
    
    cursor = conexao.cursor(dictionary=True)

    print("Teste")
    
    cursor.execute(
        """
        DROP DATABASE IF EXISTS Cinemaps;

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
            duracao TEXT NOT NULL,
            id_genero INT NOT NULL,
            foto TEXT,
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
