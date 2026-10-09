"""Создание, печать и хранение заказов."""

import json
from pathlib import Path
from typing import Any

from src.cart import cart_total


def create_order(cart: list[dict[str, Any]], client_name: str, products: list[dict[str, Any]]) -> dict[str, Any] | None:
    if not cart or not client_name.strip():
        return None
    product_ids = {product.get("id") for product in products}
    if any(item.get("id") not in product_ids or not item.get("name") for item in cart):
        return None
    return {
        "client_name": client_name.strip(),
        "items": [dict(item) for item in cart],
        "total": cart_total(cart),
    }


def print_order(order: dict[str, Any]) -> str:
    lines = [f"Заказ клиента: {order['client_name']}"]
    lines.extend(
        f"- {item['name']} (размер {item.get('size')}): {item['quantity']} × {item['price']}"
        for item in order["items"]
    )
    lines.append(f"Итого: {order['total']:.2f}")
    output = "\n".join(lines)
    print(output)
    return output


def save_orders(orders: list[dict[str, Any]], filename: str | Path) -> None:
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(orders, file, ensure_ascii=False, indent=2)


def load_orders(filename: str | Path) -> list[dict[str, Any]]:
    with Path(filename).open(encoding="utf-8") as file:
        orders = json.load(file)
    if not isinstance(orders, list):
        raise ValueError("Файл заказов должен содержать JSON-массив")
    return orders
