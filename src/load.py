import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def saveCsv(df: pd.DataFrame, nome_arquivo: str, separator: str, dec: str):
    """
    Salva um DataFrame em um arquivo CSV.

    Parâmetros:
    df (pd.DataFrame): DataFrame contendo os dados a serem salvos.
    nome_arquivo (str): Nome do arquivo CSV onde os dados serão armazenados.
    separador (str, opcional): Caractere usado como delimitador de colunas no CSV. Padrão é ",".
    decimal (str, opcional): Caractere usado para representar casas decimais. Padrão é ".".
    """
    df.to_csv(nome_arquivo, sep=separator, decimal=dec)
    return


def saveSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):
    """
    Salva um DataFrame em um banco de dados SQLite.

    Parâmetros:
    df (pd.DataFrame): DataFrame contendo os dados a serem salvos.
    nome_banco (str): Caminho ou nome do arquivo do banco de dados SQLite.
    nome_tabela (str): Nome da tabela onde os dados serão armazenados.
    """
    conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)

    conn.close()
    return


def saveMySQL(
    df: pd.DataFrame, usuario: str, senha: str, host: str, banco: str, nome_tabela: str):
    """
    Salva um DataFrame em um banco de dados MySQL.

    Parâmetros:
    df (pd.DataFrame): DataFrame contendo os dados a serem salvos.
    usuario (str): Nome de usuário para autenticação no banco de dados.
    senha (str): Senha para autenticação no banco de dados.
    host (str): Endereço do servidor MySQL (por exemplo, "localhost").
    banco (str): Nome do banco de dados onde os dados serão armazenados.
    nome_tabela (str): Nome da tabela onde os dados serão armazenados.
    """
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")

    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)

    return
