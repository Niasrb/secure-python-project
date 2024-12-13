from flask import Flask, jsonify

app = Flask(__name__)

# Nouvelle route racine
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API"})

# Routes existantes
@app.route('/api/health')
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/api/data')
def get_data():
    data = {
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"}
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)