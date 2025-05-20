import pandas as pd
import requests
from datetime import datetime

def transacoes_pix_ultimos_5_anos() -> pd.DataFrame:
    """
    Modo adulterado.
    Extrai dados de transações Pix dos últimos 5 anos (todos os meses) da API do Banco Central.
    
    Retorna:
        pd.DataFrame: Dados combinados em um único DataFrame.
    """
    # Define o intervalo: janeiro de 2020 até o mês atual
    hoje = datetime.today()
    start_year = 2020
    end_year = hoje.year
    end_month = hoje.month

    # Gera todos os valores de AnoMes no formato AAAAMM
    ano_mes_list = []
    for ano in range(start_year, end_year + 1):
        for mes in range(1, 13):
            if ano == end_year and mes > end_month:
                break
            ano_mes = f"{ano}{mes:02d}"
            ano_mes_list.append(ano_mes)

    # Monta o filtro com operadores OR
    filtro = " or ".join([f"AnoMes eq {am}" for am in ano_mes_list])

    # Cria a URL com todos os meses no filtro
    url = (
        "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/"
        f"EstatisticasTransacoesPix(Database=@Database)?@Database='{ano_mes_list[-1]}'"
        f"&$top=10000"
        f"&$format=json"
        f"&$select=AnoMes,PAG_PFPJ,REC_PFPJ,PAG_REGIAO,REC_REGIAO,"
        f"PAG_IDADE,REC_IDADE,FORMAINICIACAO,NATUREZA,FINALIDADE,VALOR,QUANTIDADE"
        f"&$filter={filtro}"
    )

    # Faz a requisição
    req = requests.get(url)
    print("Status Code:", req.status_code)

    # Trata a resposta
    if req.status_code == 200:
        try:
            data = req.json()
            if 'value' in data:
                df = pd.json_normalize(data['value'])
                return df
            else:
                print("Erro: Chave 'value' não encontrada na resposta.")
                return pd.DataFrame()
        except ValueError:
            print("Erro ao desserializar o JSON.")
            return pd.DataFrame()
    else:
        print(f"Erro na requisição. Código de status: {req.status_code}")
        return pd.DataFrame()

# Executa e imprime
df = transacoes_pix_ultimos_5_anos()
print(df)

