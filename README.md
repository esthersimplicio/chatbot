Chatbot

Este projeto é um chatbot simples desenvolvido em Python usando Flask para o backend e jQuery para o frontend interativo. O chatbot realiza análise de sentimento nas mensagens enviadas e fornece respostas personalizadas com base nessa análise.

Estrutura do Projeto
backend: Contém o código do servidor Flask e os modelos de análise de sentimento.

app.py: Arquivo principal do servidor Flask.
models: Diretório que armazena modelos pré-treinados e vetores TF-IDF para análise de sentimento.
templates: Diretório contendo o arquivo HTML para a interface do chatbot.
frontend: Contém o código do frontend, incluindo estilos CSS.

css/index.css: Estilos CSS para o frontend.
index.html: Arquivo HTML para a interface do chatbot.
tests: Contém testes unitários para o aplicativo Flask.

test_app.py: Arquivo de teste contendo casos de teste para as rotas do aplicativo Flask.
README.md: Documentação principal do projeto.

Configuração do Ambiente
Certifique-se de ter o Python instalado. Recomenda-se o uso de um ambiente virtual.

bash
Copy code
python -m venv venv
source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'
Instale as dependências do Flask.

bash
Copy code
pip install -r requirements.txt
Execução do Aplicativo
Navegue até o diretório backend.

bash
Copy code
cd backend
Execute o aplicativo Flask.

bash
Copy code
python app.py
Abra o navegador e acesse http://127.0.0.1:5000 para interagir com o chatbot.

Execução dos Testes
Navegue até o diretório tests.

bash
Copy code
cd tests
Execute os testes usando o pytest.

bash
Copy code
pytest
Link do GitHub
O código-fonte completo do projeto está disponível no GitHub. Você pode acessar o repositório aqui (https://github.com/esthersimplicio/chatbot) . 
