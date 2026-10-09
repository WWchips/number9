import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from src.orders import create_order, load_orders, print_order, save_orders


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.products = [{"id": 1, "name": "Кроссовки", "price": 100}]
        self.cart = [{"id": 1, "name": "Кроссовки", "size": 40, "price": 100, "quantity": 2}]

    def test_create_order_total(self):
        order = create_order(self.cart, "Иван", self.products)
        self.assertEqual(order["total"], 200)

    def test_empty_order_is_rejected(self):
        self.assertIsNone(create_order([], "Иван", self.products))

    def test_save_load_and_print_order(self):
        order = create_order(self.cart, "Иван", self.products)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "orders.json"
            save_orders([order], path)
            self.assertEqual(load_orders(path), [order])
        with redirect_stdout(StringIO()):
            self.assertIn("Итого: 200.00", print_order(order))


if __name__ == "__main__":
    unittest.main()
