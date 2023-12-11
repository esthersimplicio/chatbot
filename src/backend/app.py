from flask import Flask, redirect, render_template, url_for, request, jsonify
import joblib
import os

app = Flask(__name__, template_folder='templates')

base_path = os.path.abspath(os.path.dirname(__file__))
models_path = os.path.join(base_path, 'models') 

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

# Função para carregar o modelo
def load_model():
    model_path = os.path.join(models_path, 'sentiment_analysis_model.pkl')
    vectorizer_path = os.path.join(models_path, 'tfidf_vectorizer.pkl')

    model = joblib.load(open(model_path, 'rb'))
    vectorizer = joblib.load(open(vectorizer_path, 'rb'))

    return model, vectorizer

# Carrega o modelo e o vetorizador
model, vectorizer = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json['data']
        # Pré-processa e vetoriza os dados
        data_vectorized = vectorizer.transform([data])
        # Faz a predição
        prediction = model.predict(data_vectorized)

        # Adicione logs
        print(f'Dados recebidos: {data}')
        print(f'Predição: {prediction[0]}')

        # Retorna o resultado como JSON
        return jsonify({'sentiment': prediction[0]})
    except Exception as e:
        # Registre detalhes do erro
        print(f"Erro na rota /predict: {str(e)}")
        return jsonify({'error': 'Ocorreu um erro interno'}), 500

if __name__ == '__main__':
    app.run(debug=True)
