import os
import json
from flask import Flask, jsonify, request

server = Flask(__name__)

# Determine the path to the JSON file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'customers.json')

# Load customer data from file
def load_customers():
    try:
        with open(server.config.get('DATA_FILE', DATA_FILE), 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save customer data to file
def save_customers(customers):
    with open(server.config.get('DATA_FILE', DATA_FILE), 'w') as file:
        json.dump(customers, file, indent=4)

# Initialize customers data
customers = load_customers()

@server.route('/api/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

@server.route('/api/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = customers.get(customer_id)
    if customer:
        return jsonify(customer)
    else:
        return jsonify({"error": "Customer not found"}), 404

@server.route('/api/customers', methods=['POST'])
def add_customer():
    new_customer = request.json
    new_id = str(len(customers) + 1)
    customers[new_id] = new_customer
    save_customers(customers)
    return jsonify({"id": new_id, "customer": new_customer}), 201

@server.route('/api/customers/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    if customer_id in customers:
        updated_customer = request.json
        customers[customer_id] = updated_customer
        save_customers(customers)
        return jsonify({"id": customer_id, "customer": updated_customer})
    else:
        return jsonify({"error": "Customer not found"}), 404

@server.route('/api/customers/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    if customer_id in customers:
        del customers[customer_id]
        save_customers(customers)
        return jsonify({"message": "Customer deleted"})
    else:
        return jsonify({"error": "Customer not found"}), 404

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=5000)
