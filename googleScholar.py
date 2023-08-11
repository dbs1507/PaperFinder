from serpapi import GoogleSearch
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def obter_dados_google(palavra_chave, pagina=1):
    pagina = int(pagina)
    params = {
        "engine": "google_scholar",
        "q": palavra_chave,
        "api_key": os.getenv("API_KEY"),
        "start": (pagina - 1) * 10
    }

    paginationResponses = []

    paginationResponse = requests.get(
        "https://serpapi.com/search.json", params=params).json()

    paginationResponseData = {
        "organic_results": paginationResponse["organic_results"],
        "page": str(pagina)
    }
    paginationResponses.append(paginationResponseData)
    totalResults = paginationResponse["search_information"]["total_results"]
    # # for cited in paginationResponses:
    # #     for item in cited['organic_results']:
    # #         citedResponses.append(item['inline_links']['cited_by']['total'])

    # paginationResponses.insert(
    #     0, {"organic_results": organic_results, "page": "1"})

    return totalResults, paginationResponses


def citacoes(palavra_chave, page, artigo, id):
    # dado = request.args.get('dado')
    # page = request.args.get('page', 1)
    # serpapi_scholar_link = request.args.get('serpapi_scholar_link')

    params = {
        "engine": "google_scholar",
        "q": palavra_chave,
        "api_key": os.getenv("API_KEY"),
        # "start": (int(pagina) - 1) * 10
    }

    paginationResponses = []

    paginationResponses = requests.get(
        f"https://serpapi.com/search.json?cites={id}", params=params).json()

    print(paginationResponses["organic_results"])

    # paginationResponseData = {
    #     "organic_results": paginationResponse["organic_results"],
    #     "page": str(pagina)
    # }
    # paginationResponses.append(paginationResponseData)
    # totalResults = paginationResponse["search_information"]["total_results"]

    return paginationResponses
