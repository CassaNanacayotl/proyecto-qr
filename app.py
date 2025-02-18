from flask import Flask, request, jsonify
from dotenv import load_dotenv
from database import init_db, get_db
import os
from datetime import datetime
import sqlite3

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Movemos la inicialización dentro de una función
def initialize_database():
    with app.app_context():
        init_db()

# Ruta para inicializar la base de datos
@app.route('/init-db')
def setup_database():
    initialize_database()
    return jsonify({"message": "Base de datos inicializada"})

@app.route('/')
def home():
    return "Sistema QR funcionando - versión con base de datos"

@app.route('/generate-qr', methods=['POST'])
def generate_qr():
    try:
        data = request.get_json()
        
        # Verificar datos requeridos
        if not all(k in data for k in ['name', 'email']):
            return jsonify({'error': 'Faltan datos requeridos'}), 400
        
        # Generar ticket_id único
        ticket_id = f"EVT{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Conectar a la base de datos
        db = get_db()
        cursor = db.cursor()
        
        # Insertar nuevo registro
        cursor.execute('''
            INSERT INTO qr_codes (ticket_id, name, email, created_at, verification_code)
            VALUES (?, ?, ?, ?, ?)
        ''', (ticket_id, data['name'], data['email'], 
              datetime.now().isoformat(), 
              'TEMP_CODE'))
        
        db.commit()
        
        return jsonify({
            'status': 'success',
            'ticket_id': ticket_id,
            'message': 'QR pendiente de generación'
        })
        
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Error de integridad en la base de datos'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if 'db' in locals():
            db.close()

if __name__ == '__main__':
    app.run()