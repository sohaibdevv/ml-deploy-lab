```markdown
# Iris Species Predictor API 🚀

A containerized Machine Learning microservice that serves a Logistic Regression model trained on the Iris dataset. This project demonstrates an end-to-end ML deployment pipeline using **Flask** and **Docker**.

## 🛠️ Tech Stack
* **Language:** Python 3.9
* **Framework:** Flask (REST API)
* **ML Library:** Scikit-Learn
* **Containerization:** Docker

## 📂 Project Structure
* `train.py`: Script to train the model and export it as a `.pkl` file.
* `serve_model.py`: Flask application to handle inference requests.
* `Dockerfile`: Instructions to build the container image.
* `requirements.txt`: Python dependencies.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Docker Desktop installed and running

### 1. Set Up Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the Model
```bash
python train.py
```

### 4. Build the Docker Image
```bash
docker build -t iris-service .
```

### 5. Run the Container
```bash
docker run -p 80:80 iris-service
```

## 📡 API Usage

### Health Check
```bash
curl http://localhost/health
```

### Make Prediction
```bash
curl -X POST http://localhost/predict \
  -H "Content-Type: application/json" \
  -d '{"data": [5.1, 3.5, 1.4, 0.2]}'
```

Expected response:
```json
{
  "prediction": 0,
  "status": "success"
}
```

*Prediction values: 0=setosa, 1=versicolor, 2=virginica*

## 🧪 Testing the API

Send a POST request to the `/predict` endpoint with the sepal/petal measurements:

```bash
curl -X POST http://localhost:80/predict \
     -H "Content-Type: application/json" \
     -d '{"data": [5.1, 3.5, 1.4, 0.2]}'

```

### Expected Response:

```json
{
  "prediction": 0
}

```

*(Where 0: Setosa, 1: Versicolour, 2: Virginica)*

### Monitoring & Health Checks
You can verify the container's health by hitting the `/health` endpoint:

```bash
curl http://localhost:80/health