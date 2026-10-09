"""Поиск и аналитика каталога."""

from collections.abc import Iterable
from typing import Any


def _stock(product: dict[str, Any]) -> int:
    sizes = product.get("sizes")
    if isinstance(sizes, dict):
        return sum(int(amount) for amount in sizes.values())
    return int(product.get("quantity", product.get("stock", 0)))


def get_low_stock(products: Iterable[dict[str, Any]], limit: int = 3) -> list[dict[str, Any]]:
    matches = [product for product in products if _stock(product) <= limit]
    return sorted(matches, key=lambda p: (_stock(p), str(p.get("name", "")).casefold()))


def search_advanced(
    products: Iterable[dict[str, Any]], query: str = "", category: str | None = None,
    min_price: float | None = None, max_price: float | None = None,
) -> list[dict[str, Any]]:
    if min_price is not None and max_price is not None and min_price > max_price:
        raise ValueError("min_price не может быть больше max_price")
    needle = query.casefold().strip()
    if not needle:
        return []
    found = []
    for product in products:
        words = f"{product.get('name', '')} {product.get('brand', '')}".casefold()
        price = float(product.get("price", 0))
        if needle not in words:
            continue
        if category is not None and str(product.get("category", "")).casefold() != category.casefold():
            continue
        if min_price is not None and price < min_price:
            continue
        if max_price is not None and price > max_price:
            continue
        found.append(product)
    return found


def count_by_category(products: Iterable[dict[str, Any]]) -> dict[str, int]:
    result: dict[str, int] = {}
    for product in products:
        category = str(product.get("category", "Без категории"))
        result[category] = result.get(category, 0) + 1
    return result


def avg_price(products: Iterable[dict[str, Any]]) -> float:
    prices = [float(product.get("price", 0)) for product in products]
    return sum(prices) / len(prices) if prices else 0.0
