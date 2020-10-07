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

    def test_read_by_id(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        self.assertEquals(product, { 'id': 1, 'name': 'Skello' })

    def test_read_by_id_not_found(self):
        response = self.client.get("/api/v1/products/9999999")
        status_code = response.status_code
        self.assertEquals(status_code, 404)

    def test_delete_product(self):
        response = self.client.delete("/api/v1/products/5")
        status_code = response.status_code
        response_body = response.json
        self.assertEquals(status_code, 204)
        self.assertEquals(response_body, None)

    def test_create_product(self):
        payload = {'name': 'myCreatedProduct'}
        response = self.client.post("/api/v1/products", json=payload)
        status_code = response.status_code
        new_product =  response.json
        for _id in new_product.keys():
            new_product_id = _id
        self.assertEquals(
            new_product,
            {
                new_product_id: {
                    "id": int(new_product_id),
                    "name": "myCreatedProduct"
                }
            }
        )
        self.assertEquals(status_code, 201)

    def test_create_product_bad_request(self):
        payload = {'name': 'Socialive.tv'}
        response = self.client.post("/api/v1/products", json=payload)
        print(response.status_code)
        status_code = response.status_code
        new_product =  response.json
        self.assertEquals(new_product, None)
        self.assertEquals(status_code, 403)
