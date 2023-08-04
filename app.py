from flask import Flask, render_template, request
from pytrends.request import TrendReq
import trendsInterface
import googleScholar
import json
import requests

app = Flask(__name__)


def custom_filter(results):
    # Filtrar resultados que possuem 'cited_by'
    filtered_results = [
        result for result in results if 'cited_by' in result['inline_links']]
    # Ordenar os resultados filtrados pelo número de citações
    sorted_results = sorted(
        filtered_results, key=lambda x: x['inline_links']['cited_by']['total'], reverse=True)
    # Adicionar resultados com 0 citações
    for result in results:
        if 'cited_by' not in result['inline_links']:
            sorted_results.append(result)
    return sorted_results


# Registrar o filtro personalizado
app.add_template_filter(custom_filter)


@app.route('/')
def index():
    return render_template('index.html')


@app.route(f'/buscar', methods=['GET'])
def buscar():
    dado = request.args.get('dado')
    page = request.args.get('page', 1)

    if not dado or dado.strip() == "":
        alerta = "Pesquisa vazia, digite alguma palavra"
        return render_template('index.html', alerta=alerta)

    consultas_relacionadas = trendsInterface.obter_dados_completos(dado)
    totalResults, paginationResponses = googleScholar.obter_dados_google(
        dado, page)

    # consultas_relacionadas.drop("isPartial", axis=1, inplace=True or False)
    consultas_relacionadas = consultas_relacionadas.reset_index()
    consultas_relacionadas = consultas_relacionadas.values.tolist()
    print(totalResults)

    return render_template('resultado.html', consultas_relacionadas=list(consultas_relacionadas), google_scholar=paginationResponses, dado=dado, totalResults=totalResults)


if __name__ == '__main__':
    app.run(debug=True)
