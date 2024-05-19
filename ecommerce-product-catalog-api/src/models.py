import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/products.json')

def load_products():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_products(products):
    with open(DATA_FILE, 'w') as file:
        json.dump(products, file, indent=4)
