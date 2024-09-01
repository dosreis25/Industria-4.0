# backend.py
import csv
import os
import random
from datetime import datetime

DATA_FILE = 'data/energy_data.csv'

def init_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['timestamp', 'energy_consumption'])

def log_energy_data():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    energy_consumption = round(random.uniform(100, 500), 2)  # Simulação de consumo de energia

    with open(DATA_FILE, mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, energy_consumption])

def get_energy_data():
    with open(DATA_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Inicializa o arquivo de dados
init_data_file()
