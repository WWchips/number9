"""Аналитика сохранённых заказов."""

from collections import Counter
from collections.abc import Iterable
from typing import Any


def total_revenue(orders: Iterable[dict[str, Any]]) -> float:
    return sum(float(order.get("total", 0)) for order in orders)


def best_selling_product(orders: Iterable[dict[str, Any]]) -> str | None:
    quantities: Counter[str] = Counter()
    for order in orders:
        for item in order.get("items", []):
            name = str(item.get("name", ""))
            if name:
                quantities[name] += int(item.get("quantity", 0))
    return quantities.most_common(1)[0][0] if quantities else None


def average_order_total(orders: Iterable[dict[str, Any]]) -> float:
    totals = [float(order.get("total", 0)) for order in orders]
    return sum(totals) / len(totals) if totals else 0.0
