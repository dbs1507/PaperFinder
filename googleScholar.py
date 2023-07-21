from serpapi import GoogleSearch
import requests


def obter_dados_google(palavra_chave, pagina=1):
    pagina = int(pagina)
    params = {
        "engine": "google_scholar",
        "q": palavra_chave,
        "api_key": "5468326dba3cae3868bc9c03594d2ac4c9d3ee3136c8f34d73704c1d1ac67d46",
        "start": (pagina - 1) * 10
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results["organic_results"]

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
