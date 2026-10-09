import os
import unittest

from src.cart import add_to_cart
from src.orders import create_order, load_orders, save_orders
from src.storage import load_products


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.products = load_products("data/products.json")
        self.cart = []
        self.orders_file = "data/test_orders.json"

    def tearDown(self):
        if os.path.exists(self.orders_file):
            os.remove(self.orders_file)

    def test_full_cycle(self):
        result, message = add_to_cart(self.cart, self.products, 1, 40, 2)
        self.assertTrue(result, message)

        order = create_order(self.cart, "Тестовый клиент", self.products)
        self.assertIsNotNone(order)
        self.assertGreater(order["total"], 0)

        save_orders([order], self.orders_file)
        loaded = load_orders(self.orders_file)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["total"], order["total"])
        self.assertEqual(loaded[0]["items"][0]["name"], "Кроссовки Sprint")


if __name__ == "__main__":
    unittest.main()
