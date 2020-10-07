# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask

from src.db import PRODUCTS
from src.errors import Exceptions as e

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/api/v1/products', methods=["GET"])
def read():
    return PRODUCTS


@app.route('/api/v1/products/<uuid>', methods=["GET"])
def read_by_id(uuid):
    products = read()
    product = products.get(int(uuid), None)
    if product is None:
        # return "Not found", 404
        return e.not_found_404()
    return product


@app.route('/api/v1/products/<uuid>', methods=["DELETE"])
def delete_by_id(uuid):
    products = read()
    product = products.get(int(uuid), None)
    if product is None:
        return e.not_found_404()
    del products[int(uuid)]
    return e.deleted_204()

