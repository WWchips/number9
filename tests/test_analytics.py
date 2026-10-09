import unittest

from src.analytics import average_order_total, best_selling_product, total_revenue


class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.orders = [
            {"total": 300, "items": [{"name": "Кроссовки", "quantity": 2}]},
            {"total": 100, "items": [{"name": "Кроссовки", "quantity": 1}, {"name": "Мяч", "quantity": 1}]},
        ]

    def test_total_revenue(self):
        self.assertEqual(total_revenue(self.orders), 400)

    def test_best_selling_product(self):
        self.assertEqual(best_selling_product(self.orders), "Кроссовки")

    def test_average_order_total(self):
        self.assertEqual(average_order_total(self.orders), 200)


if __name__ == "__main__":
    unittest.main()
