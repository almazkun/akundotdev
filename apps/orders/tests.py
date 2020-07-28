from django.test import TestCase

from .models import Order
from apps.shop.models import Product

test_order = {"name": "Django Django", "email": "django@django.some", "paid": True}

test_product = {
    "name": "Test Product",
    "abbr": "TEPR",
    "slug": "tepr",
    "description": "Test Product description",
    "price": 2000,
}

# Create your tests here.
class TestOrderModelCreation(TestCase):
    def setUp(self):
        self.test_order = test_order
        self.test_product = test_product
        Order.objects.create(
            **self.test_order, product=Product.objects.create(**self.test_product)
        )

    def test_order_model_created(self):
        obj = Order.objects.get(name=self.test_order["name"])

        self.assertEqual(obj.name, self.test_order["name"])
        self.assertEqual(obj.email, self.test_order["email"])
        self.assertEqual(obj.paid, self.test_order["paid"])
        self.assertEqual(obj.product.name, self.test_product["name"])
