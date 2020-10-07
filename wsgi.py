# wsgi.py
# pylint: disable=missing-docstring

import itertools

from flask import (
    Flask,
    request,
    jsonify
)


from src.db import PRODUCTS as products
from src.responses import Responses as resp


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def read():
    return products


@app.route('/api/v1/products/<uuid>', methods=["GET"])
def read_by_id(uuid):
    products = read()
    product = products.get(int(uuid), None)
    if product is None:
        return resp.not_found_404()
    return product


@app.route('/api/v1/products/<uuid>', methods=["DELETE"])
def delete_by_id(uuid):
    products = read()
    product = products.get(int(uuid), None)
    if product is None:
        return resp.not_found_404()
    del products[int(uuid)]
    return resp.deleted_204()

@app.route('/api/v1/products', methods=["POST"])
def create():
    products = read()
    body = request.get_json()
    for product in products.items():
        if body["name"] == product[1]["name"]:
            return "Forbidden", 403
    start_index = len(products) + 1
    identifier_generator = next(itertools.count(start_index))
    new_product = {
        int(identifier_generator): {
            "id": int(identifier_generator),
            "name": body["name"],
        }
    }
    products.update(new_product)
    return new_product, 201
