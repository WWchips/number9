"""Точка входа демонстрационного приложения SportShop."""

from src.analytics import total_revenue
from src.cart import add_to_cart
from src.catalog import get_low_stock, search_advanced
from src.orders import create_order, print_order
from src.storage import load_products


def main() -> None:
    products = load_products("data/products.json")
    print(f"Загружено товаров: {len(products)}")
    print("Низкий остаток:", ", ".join(p["name"] for p in get_low_stock(products)))
    print("Поиск обуви:", ", ".join(p["name"] for p in search_advanced(products, "кроссовки")))

    cart = []
    added, message = add_to_cart(cart, products, 1, 40, 2)
    print(message)
    if added:
        order = create_order(cart, "Демо-клиент", products)
        if order:
            print_order(order)
            print(f"Выручка демонстрационного заказа: {total_revenue([order]):.2f}")


if __name__ == "__main__":
    main()
