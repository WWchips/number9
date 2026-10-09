import unittest

from src.catalog import avg_price, count_by_category, get_low_stock, search_advanced


class TestCatalog(unittest.TestCase):
    def setUp(self):
        self.products = [
            {"id": 1, "name": "Кроссовки Sprint", "brand": "SportPro", "category": "Обувь", "price": 100, "sizes": {40: 2}},
            {"id": 2, "name": "Футболка Run", "brand": "Active", "category": "Одежда", "price": 300, "quantity": 8},
        ]

    def test_low_stock_uses_sizes_and_sorts(self):
        self.assertEqual([p["id"] for p in get_low_stock(self.products)], [1])

    def test_search_by_name_and_filters(self):
        self.assertEqual(len(search_advanced(self.products, "кроссовки", category="Обувь", min_price=90)), 1)

    def test_invalid_price_range(self):
        with self.assertRaises(ValueError):
            search_advanced(self.products, "run", min_price=500, max_price=100)

    def test_category_counts_and_average_price(self):
        self.assertEqual(count_by_category(self.products), {"Обувь": 1, "Одежда": 1})
        self.assertEqual(avg_price(self.products), 200)


if __name__ == "__main__":
    unittest.main()
