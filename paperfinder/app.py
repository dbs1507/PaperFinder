from flask import Flask, render_template, request
from pytrends.request import TrendReq
import trendsInterface
import googleScholar
import json
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route(f'/buscar', methods=['GET'])
def buscar():
    dado = request.args.get('dado')
    page = request.args.get('page', 1)
    consultas_relacionadas = trendsInterface.obter_dados_completos(dado)
    totalResults, paginationResponses = googleScholar.obter_dados_google(
        dado, page)  # Adicionando a variável pagination

    consultas_relacionadas.drop("isPartial", axis=1, inplace=True or False)
    consultas_relacionadas = consultas_relacionadas.reset_index()
    consultas_relacionadas = consultas_relacionadas.values.tolist()
    print(totalResults)

    return render_template('resultado.html', consultas_relacionadas=list(consultas_relacionadas), google_scholar=paginationResponses, dado=dado, totalResults=totalResults)


if __name__ == '__main__':
    app.run(debug=True)
