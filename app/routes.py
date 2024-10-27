from flask import Flask, jsonify
from flask_jwt_extended import jwt_required
from app.scraping import obter_dados_producao, obter_dados_processamento, obter_dados_comercializacao, obter_dados_exportacao, obter_dados_importacao

app = Flask(__name__)

@app.route('/producao', methods=['GET'])
@jwt_required()
def producao():  
    dados = obter_dados_producao()
    return jsonify(dados)


@app.route('/processamento', methods=['GET'])
@jwt_required()  # Protege a rota com JWT
def processamento():
    dados = obter_dados_processamento()
    return jsonify(dados)

@app.route('/comercializacao', methods=['GET'])
@jwt_required()  # Protege a rota com JWT
def comercializacao():
    dados = obter_dados_comercializacao()
    return jsonify(dados)

@app.route('/exportacao', methods=['GET'])
@jwt_required()  # Protege a rota com JWT
def exportacao():
    dados = obter_dados_exportacao()
    return jsonify(dados)

@app.route('/importacao', methods=['GET'])
@jwt_required()  # Protege a rota com JWT
def importacao():
    dados = obter_dados_importacao()
    return jsonify(dados)
