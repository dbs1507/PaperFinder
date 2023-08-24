from serpapi import GoogleSearch
import pandas as pd
from dateutil.parser import parse
import os
from dotenv import load_dotenv

load_dotenv()


def obter_dados_completos(palavra_chave):
    params = {
        "engine": "google_trends",
        "q": palavra_chave,
        "data_type": "TIMESERIES",
        "api_key": os.getenv("API_KEY"),
        "date": "today 12-m",

    }

    search = GoogleSearch(params)
    results = search.get_dict()
    interest_over_time = results.get("interest_over_time")

    if interest_over_time is None:
        return None  # Retorna None se interest_over_time estiver vazio

    dados_outra_api = interest_over_time.get('timeline_data')

    if dados_outra_api is None:
        return None  # Retorna None se dados_outra_api estiver vazio

    # Criar listas para armazenar os dados 'date' e 'value'
    dates = []
    values = []

    # Percorrer o DataFrame e extrair os dados 'date' e 'value'
    for entry in dados_outra_api:
        for value_entry in entry['values']:
            dates.append(parse(entry['date'].split('–')[0].strip()))
            values.append(int(value_entry['value']))

    # Criar um novo DataFrame a partir das listas
    consultas_relacionadas = pd.DataFrame({'date': dates, 'value': values})

    return consultas_relacionadas
