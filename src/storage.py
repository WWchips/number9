"""Чтение и запись данных SportShop в JSON."""

import json
from pathlib import Path
from typing import Any


def load_products(filename: str | Path) -> list[dict[str, Any]]:
    with Path(filename).open(encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("Файл товаров должен содержать JSON-массив")
    return data


def save_products(products: list[dict[str, Any]], filename: str | Path) -> None:
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=2)
