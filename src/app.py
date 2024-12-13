"""
Flask application providing REST API endpoints for health check and data retrieval.
This module implements a simple Flask server with basic endpoints.
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """
    Root endpoint that returns a welcome message.
    Returns:
        dict: A JSON response with a welcome message
    """
    return jsonify({"message": "Welcome to the API"})

@app.route('/api/health')
def health_check():
    """
    Health check endpoint to verify the API status.
    Returns:
        dict: A JSON response indicating the health status
    """
    return jsonify({"status": "healthy"})

@app.route('/api/data')
def get_data():
    """
    Data endpoint that returns a list of sample items.
    Returns:
        dict: A JSON response containing sample data items
    """
    data = {
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"}
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
