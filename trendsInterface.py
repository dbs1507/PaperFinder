# from pytrends.request import TrendReq


# def obter_dados_completos(palavra_chave):
#     pytrends = TrendReq(hl='pt-BR', tz=360)
#     pytrends.build_payload(
#         [palavra_chave], timeframe='today 12-m', geo='BR', gprop='')
#     consultas_relacionadas = pytrends.interest_over_time()

#     print(type(consultas_relacionadas))

#     return consultas_relacionadas

# from serpapi import GoogleSearch


# def obter_dados_completos(palavra_chave):
#     params = {
#         "engine": "google_trends",
#         "q": palavra_chave,
#         "data_type": "TIMESERIES",
#         "api_key": "5468326dba3cae3868bc9c03594d2ac4c9d3ee3136c8f34d73704c1d1ac67d46",
#         "date": "today 12-m",
#     }

#     search = GoogleSearch(params)
#     results = search.get_dict()
#     interest_over_time = results["interest_over_time"]

#     extracted_data = [(entry['values'][0]['value'], entry['date'])
#                       for entry in interest_over_time['timeline_data']]

#     # Printing the extracted data
#     for value, date in extracted_data:


#         return value, date

from serpapi import GoogleSearch
import pandas as pd
from dateutil.parser import parse


def obter_dados_completos(palavra_chave):
    params = {
        "engine": "google_trends",
        "q": palavra_chave,
        "data_type": "TIMESERIES",
        "api_key": "5468326dba3cae3868bc9c03594d2ac4c9d3ee3136c8f34d73704c1d1ac67d46",
        "date": "today 12-m",

    }

    search = GoogleSearch(params)
    results = search.get_dict()
    interest_over_time = results["interest_over_time"]

    dados_outra_api = interest_over_time['timeline_data']

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
