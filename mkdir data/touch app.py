# app.py
from flask import Flask, jsonify
from backend import log_energy_data, get_energy_data
import time
import threading

app = Flask(__name__)

@app.route('/api/energy_data', methods=['GET'])
def energy_data():
    data = get_energy_data()
    return jsonify(data)

def generate_data():
    while True:
        log_energy_data()
        time.sleep(5)  # Gera novos dados a cada 5 segundos

if __name__ == '__main__':
    threading.Thread(target=generate_data).start()
    app.run(debug=True)
