from flask import Flask, jsonify, request, send_from_directory
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_swagger_ui import get_swaggerui_blueprint
from app.routes import app

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta_super_secreta'  # Defina uma chave secreta forte
jwt = JWTManager(app)

# Rota de login para gerar o token JWT
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Verificação simples de usuário (você pode substituir por autenticação baseada em banco de dados)
    if username != 'admin' or password != 'senha123':
        return jsonify({"msg": "Usuário ou senha incorretos"}), 401

    # Cria o token de acesso
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

# Configurações do Swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # Caminho para o arquivo swagger.json

# Configura o Swagger UI
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API de Vitivinicultura"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Rota para servir arquivos estáticos (swagger.json)
@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)

# Inicia o aplicativo
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
