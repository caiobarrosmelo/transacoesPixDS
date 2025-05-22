import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def saveCsv(df: pd.DataFrame, nome_arquivo: str, separator: str, dec: str):
    df.to_csv(nome_arquivo, sep=separator, decimal=dec)
    return


def saveSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):

    conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)

    conn.close()
    return


def saveMySQL(
    df: pd.DataFrame, usuario: str, senha: str, host: str, banco: str, nome_tabela: str):
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")

    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)

    return
