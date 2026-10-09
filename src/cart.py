"""Операции с корзиной."""

from collections.abc import Iterable
from typing import Any

from src.catalog import _stock


def _find_product(products: Iterable[dict[str, Any]], product_id: Any) -> dict[str, Any] | None:
    return next((product for product in products if product.get("id") == product_id), None)


def _find_item(cart: list[dict[str, Any]], product_id: Any, size: Any) -> dict[str, Any] | None:
    return next((item for item in cart if item.get("id") == product_id and item.get("size") == size), None)


def add_to_cart(
    cart: list[dict[str, Any]], products: Iterable[dict[str, Any]],
    product_id: Any, size: Any, quantity: int,
) -> tuple[bool, str]:
    product = _find_product(products, product_id)
    if product is None:
        return False, "Товар не найден"
    if quantity <= 0:
        return False, "Количество должно быть положительным"

    sizes = product.get("sizes")
    if isinstance(sizes, dict):
        size_key = next((key for key in sizes if str(key) == str(size)), None)
        if size_key is None:
            return False, "Такого размера нет у товара"
        size = size_key
        available = int(sizes[size])
    else:
        available = _stock(product)

    existing = _find_item(cart, product_id, size)
    current_qty = int(existing.get("quantity", 0)) if existing else 0
    if current_qty + quantity > available:
        return False, "Недостаточно товара в наличии"
    if existing:
        existing["quantity"] = current_qty + quantity
    else:
        cart.append({
            "id": product_id,
            "name": product.get("name", ""),
            "size": size,
            "price": float(product.get("price", 0)),
            "quantity": quantity,
        })
    return True, "Товар добавлен в корзину"


def remove_from_cart(cart: list[dict[str, Any]], product_id: Any, size: Any) -> bool:
    item = _find_item(cart, product_id, size)
    if item is None:
        return False
    cart.remove(item)
    return True


def update_quantity(
    cart: list[dict[str, Any]], products: Iterable[dict[str, Any]],
    product_id: Any, size: Any, new_qty: int,
) -> bool:
    item = _find_item(cart, product_id, size)
    product = _find_product(products, product_id)
    if item is None or product is None or new_qty <= 0:
        return False
    sizes = product.get("sizes")
    if isinstance(sizes, dict):
        key = next((key for key in sizes if str(key) == str(size)), None)
        if key is None or new_qty > int(sizes[key]):
            return False
    elif new_qty > _stock(product):
        return False
    item["quantity"] = new_qty
    return True


def cart_total(cart: Iterable[dict[str, Any]]) -> float:
    return sum(float(item.get("price", 0)) * int(item.get("quantity", 1)) for item in cart)
