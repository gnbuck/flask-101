# tests/test_views.py
from flask_testing import TestCase
from wsgi import app


class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, dict)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.
        self.assertEquals(products["1"], { 'id': 1, 'name': 'Skello' })

    def test_read_existing_product(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        self.assertEquals(product, { 'id': 1, 'name': 'Skello' })

    def test_read_missing_product(self):
        response = self.client.get("/api/v1/products/9999999")
        status_code = response.status_code
        self.assertEquals(status_code, 404)

    def test_delete_product(self):
        response = self.client.delete("/api/v1/products/5")
        status_code = response.status_code
        response_body = response.json
        self.assertEquals(status_code, 204)
        self.assertEquals(response_body, None)
