from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the model with error handling
MODEL_PATH = 'iris_model.pkl'

def load_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            return pickle.load(f)
    return None

model = load_model()

@app.route('/health', methods=['GET'])
def health_check():
    """Confirms the server is up and the model is loaded."""
    if model is not None:
        return jsonify({"status": "healthy", "model_loaded": True}), 200
    return jsonify({"status": "unhealthy", "reason": "Model file missing"}), 500

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not initialized"}), 500
    try:
        data = request.get_json(force=True)
        # Prediction logic
        prediction = model.predict([np.array(data['data'])])
        return jsonify({
            'prediction': int(prediction[0]),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)