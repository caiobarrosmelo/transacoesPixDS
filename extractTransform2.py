import pandas as pd
import requests

def transacoes_pix(data: str) -> pd.DataFrame:
    """
    Modo puro sangue.
    Função para extrair dados de transações do Pix do Banco Central do Brasil. 
    
    Atributo:
    String - AAAAMM - A ano e M - mês (1-12)
    
    Saída:
    DataFrame com os dados de transações do Pix.
    """
    # Monta a URL com o parâmetro "data" passado à função
    url = f"https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/EstatisticasTransacoesPix(Database=@Database)?@Database='202501'&$top=100&$format=json&$select=AnoMes,PAG_PFPJ,REC_PFPJ,PAG_REGIAO,REC_REGIAO,PAG_IDADE,REC_IDADE,FORMAINICIACAO,NATUREZA,FINALIDADE,VALOR,QUANTIDADE&$filter=AnoMes eq {data}"

    # Faz a requisição para a API
    req = requests.get(url)
    
    # Verifica o status da requisição
    print("Status Code: ", req.status_code)
    
    # Verifica se o status da requisição foi bem-sucedido (código 200)
    if req.status_code == 200:
        try:
            # Desserializa o JSON
            data = req.json()
            
            # Verifica se há dados na chave 'value' do JSON
            if 'value' in data:
                # Normaliza os dados para um DataFrame
                df = pd.json_normalize(data['value'])
                return df
            else:
                print("Erro: Chave 'value' não encontrada na resposta.")
                return pd.DataFrame()  # Retorna um DataFrame vazio
        except ValueError:
            print("Erro ao desserializar o JSON.")
            return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro
    else:
        print(f"Erro na requisição. Código de status: {req.status_code}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro na requisição

# Exemplo de uso da função
df = transacoes_pix("202501")  # Passando o valor correto do parâmetro (ano e mês)
print(df)
