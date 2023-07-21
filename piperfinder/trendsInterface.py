from pytrends.request import TrendReq


def obter_dados_completos(palavra_chave):
    pytrends = TrendReq(hl='pt-BR', tz=360)
    pytrends.build_payload(
        [palavra_chave], timeframe='today 12-m', geo='BR', gprop='')
    consultas_relacionadas = pytrends.interest_over_time()

    print(consultas_relacionadas)

    return consultas_relacionadas
