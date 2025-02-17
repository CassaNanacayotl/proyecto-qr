FROM python:3.11.7-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Crear usuario no-root
RUN adduser --disabled-password --gecos '' appuser
USER appuser

COPY . .

# Especificar el puerto que Render espera
ENV PORT=10000
EXPOSE 10000

CMD gunicorn app:app --bind 0.0.0.0:$PORT