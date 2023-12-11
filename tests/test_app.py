import os
import sys

# Adiciona o diretório 'src' ao caminho do sistema, permitindo a importação do módulo 'backend'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importa o módulo pytest e a função url_for do Flask
import pytest
from flask import url_for

# Importa a instância do aplicativo Flask do módulo 'backend'
from backend.app import app

# Fixture para configurar um cliente de teste
@pytest.fixture
def client():
    # Configura o aplicativo para o modo de teste
    app.config['TESTING'] = True
    # Cria um cliente de teste
    with app.test_client() as client:
        # Retorna o cliente para ser usado nos testes
        yield client

# Teste: Verifica se a rota '/' redireciona corretamente
def test_home_redirect(client):
    # Envia uma solicitação GET para a rota '/'
    response = client.get('/')
    # Verifica se o código de status é 302 (redirecionamento)
    assert response.status_code == 302

# Teste: Verifica se a rota '/index' retorna um código de status 200
def test_index_page(client):
    # Envia uma solicitação GET para a rota '/index'
    response = client.get('/index')
    # Verifica se o código de status é 200 (sucesso)
    assert response.status_code == 200

# Teste: Verifica se a rota '/predict' retorna uma resposta esperada para uma solicitação POST
def test_predict_route(client):
    # Dados de exemplo para predição
    data = {'data': 'exemplo de dado para predição'}
    # Envia uma solicitação POST para a rota '/predict' com os dados de exemplo
    response = client.post('/predict', json=data)
    # Verifica se o código de status é 200 (sucesso)
    assert response.status_code == 200
    # Verifica se a chave 'sentiment' está presente na resposta JSON
    assert 'sentiment' in response.json
