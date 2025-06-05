import pandas as pd
import requests

def transacoes_pix(data: str) -> pd.DataFrame:
    """
    Função para extrair dados de transações do Pix do Banco Central do Brasil.

    Atributo:
    String - AAAAMM - A ano e M - mês (1-12)

    Saída:
    DataFrame com os dados de transações do Pix.
    """
    # Monta a URL com o parâmetro "data" passado à função
    url = f"https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/EstatisticasTransacoesPix(Database=@Database)?@Database='202501'&$top=10000&$format=json&$select=AnoMes,PAG_PFPJ,REC_PFPJ,PAG_REGIAO,REC_REGIAO,PAG_IDADE,REC_IDADE,FORMAINICIACAO,NATUREZA,FINALIDADE,VALOR,QUANTIDADE&$filter=AnoMes eq {data}"

    # Faz a requisição para a API
    req = requests.get(url)

    # Verifica o status da requisição
    print("Status Code: ", req.status_code)

    # Desserializa o JSON
    data = req.json()
    # Normaliza os dados para um DataFrame
    df = pd.json_normalize(data["value"])

    pd.to_datetime(df["AnoMes"], format="%Y%m")
    df["AnoMes"] = pd.to_datetime(df["AnoMes"], format="%Y%m")
    return df
