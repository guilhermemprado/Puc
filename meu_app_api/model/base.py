"""
    Imports
"""
import sqlite3

from sqlalchemy.ext.declarative import declarative_base


def create_data_base(path, nome_db):
    """
    Cria banco de dado.
    Cria tabelas: carros, marca, modelo, combustivel.
    """
    # Conectar ao banco de dados (ou criar um novo banco de dados se ele não existir)
    conexao = sqlite3.connect(path + nome_db, check_same_thread=False)

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Criar uma tabela para armazenar as marcas
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS brand 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE)
    """
    )

    # Criar uma tabela para armazenar os modelos
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS model 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            brand INTEGER,
            foreign key(brand) REFERENCES brand(id))
    """
    )

    # Criar uma tabela para armazenar os combustiveis
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS fuel 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL UNIQUE)
    """
    )

    # Criar uma tabela para armazenar os carros
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS car 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            color TEXT NOT NULL,
            year_manufacture TEXT NOT NULL,
            year_model TEXT NOT NULL,
            value REAL NOT NULL,
            model INTEGER NOT NULL,
            fuel INTEGER NOT NULL,
            foreign key(model) REFERENCES model(id)
            foreign key(fuel) REFERENCES fuel(id))
    """
    )

    # Combustível
    sql = "INSERT INTO fuel (type) VALUES {}"

    dados = """('Disel'), ('Elétrico'), ('Gasolina'), ('Gpl'), 
            ('Híbrido (Disel)'), ('Híbrido (Gasolina)')
        """
    cursor.execute(sql.format(dados))
    conexao.commit()

    # Marca
    sql = "INSERT INTO brand (name) VALUES {}"

    dados = """('Audi'), ('Bmw'), ('Chevrolet'), ('Citroën'), 
            ('Dacia'), ('Fiat'), ('Ford'), ('Jeep'), ('Kia'), 
            ('Mercedez-Benz'), ('Mini'), ('Toyota'), ('Tesla'), 
            ('Volvo'), ('Vw'), ('Skoda')
        """
    cursor.execute(sql.format(dados))
    conexao.commit()

    # Modelo
    sql = "INSERT INTO model (name, brand) VALUES {}"

    dados = """('A3 2.0 tdi', 1), ('A4 2.0 tdi s-line', 1),
            ('318 Serie 3 touring advantage 2.0 hdi', 2), ('116 serie 1 1.5 hdi', 2), 
            ('Sandero 1.0 sce stepway', 5), ('Duster 1.3 tce prestige', 5),
            ('V40 2.0 d2 momentum eco', 14), ('S40 1.6 d', 14),
            ('Panda 1.0', 6), ('500 1.2 lounge', 6),
            ('Fiesta 1.0t ecoboost titanium', 7), ('Courier 1.5 hdi', 7),
            ('Ceed sw 1.0 t-gdi sport', 9), ('E-soul aut', 9), 
            ('Cla 200 brake dct 1.9', 10), ('Glc 2500 exclusive 4-matic', 10),
            ('Auris touring 1.8 hsg cmfort', 12), ('Corolla 2.0 d-4d hdi', 12),
            ('Golf variant 1.6 tdi highline', 15), ('Polo 1.4 tdi blue motion', 15),
            ('Octavia break 1.6 tdi ambition', 16), ('Scala 1.0 tsi', 16),
            ('Model 3 tração taseira', 13), 
            ('Clubman one d 1.5 hdi', 11),
            ('Ds4 1.6 e-hdi so chic etg6', 4)
        """
    cursor.execute(sql.format(dados))
    conexao.commit()

    # Carro
    sql = "INSERT INTO car (color, year_manufacture, year_model, value, model, fuel) VALUES {}"

    dados = """('Branco', 2000, 2000, 9500.00, 1, 1),
            ('Cinza', 2005, 2006, 14900.00, 3, 1),
            ('Preto', 2012, 2012, 3750.00, 11, 3),
            ('Prata', 2008, 2009, 8600.00, 12, 1),
            ('Azul', 2020, 2020, 16000.00, 13, 3),
            ('Vermelho', 2020, 2021, 0.00, 17, 5),
            ('Marrom/bege', 2022, 2023, 19300.00, 14, 2),
            ('Verde', 2022, 2022, 27900.00, 7, 2),
            ('Amarelo/dourado', 2002, 2002, 19000.00, 25, 5)
    """
    cursor.execute(sql.format(dados))
    conexao.commit()


# cria uma classe Base para o instanciamento de novos objetos/tabelas
Base = declarative_base()
