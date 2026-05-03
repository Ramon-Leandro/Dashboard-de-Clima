from flask import Flask, request, jsonify   # Flask: cria o servidor; request: pega dados da URL; jsonify: converte dados para JSON
from flask_sqlalchemy import SQLAlchemy     # SQLAlchemy: Ferramenta que facilita o uso do Banco de Dados SQL
from flask_cors import CORS                 # CORS: Permite que o frontend (React) acesse o backend (Flask) mesmo estando em domínios diferentes
import requests                             # Requests: Fazer "ligações" para APIs externas (OpenWeather)
from datetime import datetime               # Datetime: Para registrar o horário exato das buscas

# --- 1. CONFIGURAÇÃO DO SERVIDOR (FLASK) ---
app = Flask(__name__)
CORS(app) # Sem isso, o navegador bloqueia a conexão entre React (porta 5173) e Python (porta 5000)

# --- 2. CONFIGURAÇÃO DO BANCO DE DADOS (SQL) ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///historico_clima.db' # 'sqlite:///historico_clima.db' é o caminho para o arquivo do banco de dados SQLite.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desativa alertas de modificação para economizar memória
db = SQLAlchemy(app)

# --- 3. MODELO DE DADOS (ESTRUTURA DA TABELA) ---
class RegistroClima(db.Model):
    id = db.Column(db.Integer, primary_key=True) # ID
    cidade = db.Column(db.String(100), nullable=False) # Cidade que foi consultada
    temperatura = db.Column(db.Float, nullable=False) # Temperatura registrada no momento da consulta
    descricao = db.Column(db.String(200), nullable=False) # Descrição do clima (ex: "céu limpo")
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow) # Data e hora da consulta, com valor padrão sendo o momento da criação do registro

# Comando que lê o código acima e cria o arquivo de banco de dados e a tabela fisicamente
with app.app_context():
    db.create_all() # Cria o banco de dados e as tabelas definidas no modelo

# Sua chave mestra para falar com a API da OpenWeather
API_KEY = "412d73b51d3524cec3b15e69b505221f"

# --- 4. ROTA: BUSCAR CLIMA E SALVAR ---
# Esta rota é chamada pelo React quando você clica no botão "Buscar"
@app.route('/clima', methods=['GET'])
def obter_clima():
    # Pega o nome da cidade enviado na URL (ex: ?cidade=Londrina)
    cidade = request.args.get('cidade')

    if not cidade:
        return jsonify({"error": "Digite uma cidade!"}), 400 # Retorna erro se a cidade não for fornecida
    
    # Monta a URL para "ligar" para a OpenWeather pedindo os dados em Celsius (metric) e Português (pt_br)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    
    # Faz a requisição e transforma a resposta gigante em um dicionário Python (JSON)
    resposta = requests.get(url).json()    

     # Se a API responder algo diferente de 200 (Sucesso), significa que a cidade não existe ou deu erro
    if resposta.get("cod") != 200:
        return jsonify({"error": "Cidade não encontrada!"}), 404 # Retorna erro se a cidade não for encontrada
    
    # Filtra apenas o que nos interessa da resposta da API
    temp = resposta["main"]["temp"] # Temperatura
    desc = resposta["weather"][0]["description"] # Descrição do clima

    # CRIAÇÃO DO REGISTRO: Prepara os dados para salvar no SQL
    novo_registro = RegistroClima(cidade=cidade, temperatura=temp, descricao=desc)

    # OPERAÇÃO DE BANCO: Adiciona na fila e confirma a gravação (commit)
    db.session.add(novo_registro)
    db.session.commit()

    # Devolve para o React apenas os dados limpos
    return jsonify({
        "cidade": cidade,
        "temperatura": temp,
        "descricao": desc,
        "mensagem": "Salvo no histórico!"
})

# --- 5. ROTA: VER O HISTÓRICO ---
# Esta rota é chamada pelo React para preencher a tabela
@app.route('/historico', methods=['GET'])
def ver_historico():
    # Consulta o banco: "Pegue todos os registros e ordene pela data mais recente"
    registros = RegistroClima.query.order_by(RegistroClima.data_criacao.desc()).all()

    # Cria uma lista vazia para organizar os dados antes de enviar
    resultado = []
    for r in registros:
        resultado.append({
            "id": r.id,
            "cidade": r.cidade,
            "temperatura": r.temperatura,
            "descricao": r.descricao,
            "data": r.data_criacao.strftime("%Y-%m-%d %H:%M:%S") # Formata a data para string legível
        })

    # Envia a lista completa para o React
    return jsonify(resultado)

# --- 6. INICIALIZAÇÃO ---
if __name__ == '__main__':
    # Roda o servidor. 'debug=True' faz o servidor reiniciar sozinho sempre que você salvar o código.
    app.run(debug=True)