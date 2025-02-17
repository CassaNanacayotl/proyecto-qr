FROM python:3.11.7-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]