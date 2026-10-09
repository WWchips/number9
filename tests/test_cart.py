import unittest

from src.cart import add_to_cart, cart_total, remove_from_cart, update_quantity


class TestCart(unittest.TestCase):
    def setUp(self):
        self.products = [{"id": 1, "name": "Кроссовки Sprint", "price": 100, "sizes": {40: 5}}]
        self.cart = []

    def test_add_product(self):
        ok, _ = add_to_cart(self.cart, self.products, 1, 40, 2)
        self.assertTrue(ok)

    def test_rejects_missing_size(self):
        ok, message = add_to_cart(self.cart, self.products, 1, 99, 1)
        self.assertFalse(ok)
        self.assertIn("размер", message.lower())

    def test_update_remove_and_total(self):
        add_to_cart(self.cart, self.products, 1, 40, 2)
        self.assertTrue(update_quantity(self.cart, self.products, 1, 40, 3))
        self.assertEqual(cart_total(self.cart), 300)
        self.assertTrue(remove_from_cart(self.cart, 1, 40))
        self.assertEqual(self.cart, [])


if __name__ == "__main__":
    unittest.main()
