# scraping.py
import requests
from bs4 import BeautifulSoup
from flask import jsonify

# Apenas para teste pois o site da empbrapa está fora do ar:
#def obter_dados_producao():
#    url = 'https://jsonplaceholder.typicode.com/todos/1'  # URL de teste temporária
#    try:
#        response = requests.get(url, timeout=10)
#        response.raise_for_status()
#        dados = response.json()
#        return dados
#    except requests.exceptions.RequestException as e:
#        return {"error": str(e)}, 500



def obter_dados_producao():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'  # URL de Produção
    return obter_dados_da_url(url)

def obter_dados_processamento():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03'  # URL de Processamento (exemplo)
    return obter_dados_da_url(url)

def obter_dados_comercializacao():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'  # URL de Comercialização (exemplo)
    return obter_dados_da_url(url)

def obter_dados_importacao():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05'  # URL de Comercialização (exemplo)
    return obter_dados_da_url(url)

def obter_dados_exportacao():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06'  # URL de Comercialização (exemplo)
    return obter_dados_da_url(url)

def obter_dados_da_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Verifica se a resposta é 200 (OK)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontra todas as tabelas na página
        tabelas = soup.find_all('table')
        dados_completos = []

        for tabela in tabelas:
            headers = [header.text.strip() for header in tabela.find_all('th')]
            rows = []
            for row in tabela.find_all('tr'):
                cells = [cell.text.strip() for cell in row.find_all('td')]
                if cells:  # Somente adiciona linhas que não estão vazias
                    rows.append(dict(zip(headers, cells)))
            if rows:
                dados_completos.append(rows)
        
        return {"dados": dados_completos}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500
