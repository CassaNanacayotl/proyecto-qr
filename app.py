from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os
from dotenv import load_load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Ruta básica para verificar que el servidor funciona
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "message": "Sistema de QR funcionando"
    })

# Ruta que recibirá el trigger para generar QR
@app.route('/generate-qr', methods=['POST'])
def generate_qr():
    try:
        # Por ahora solo verificamos que recibimos los datos
        data = request.get_json()
        return jsonify({
            "status": "success",
            "message": "Endpoint de generación de QR listo",
            "received_data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)