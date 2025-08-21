FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app
COPY data/ ./data

ENV PYTHONUNBUFFERED=1
ENV MONGO_URI="mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]