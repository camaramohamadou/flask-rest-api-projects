from flask import Blueprint, jsonify, request, abort
from src.models import load_products, save_products

main = Blueprint('main', __name__)

@main.route('/products', methods=['GET'])
def get_products():
    products = load_products()
    return jsonify(products)

@main.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    products = load_products()
    product = next((product for product in products if product['id'] == id), None)
    if product:
        return jsonify(product)
    abort(404, description="Product not found")

@main.route('/products', methods=['POST'])
def add_product():
    products = load_products()
    data = request.get_json()
    new_id = max([product['id'] for product in products] + [0]) + 1
    new_product = {
        "id": new_id,
        **data
    }
    products.append(new_product)
    save_products(products)
    return jsonify({"message": "Product added", "id": new_id}), 201

@main.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    products = load_products()
    data = request.get_json()
    product = next((product for product in products if product['id'] == id), None)
    if product:
        product.update(data)
        save_products(products)
        return jsonify({"message": "Product updated"})
    abort(404, description="Product not found")

@main.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    products = load_products()
    product = next((product for product in products if product['id'] == id), None)
    if product:
        products.remove(product)
        save_products(products)
        return jsonify({"message": "Product deleted"})
    abort(404, description="Product not found")
