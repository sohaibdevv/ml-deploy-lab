FROM python:3.9-slim

WORKDIR /app

# Copy requirements first (better for Docker caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model and the script
COPY iris_model.pkl .
COPY serve_model.py .

EXPOSE 80

CMD ["python", "serve_model.py"]