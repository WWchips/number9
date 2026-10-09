# Руководство пользователя

Запускайте примеры из корневой папки SportShop. Для командных примеров используется стандартный интерпретатор Python 3.10+.

## 1. Просмотр каталога

```python
from src.storage import load_products

products = load_products("data/products.json")
for product in products:
    print(product["id"], product["name"], product["price"], product["category"])
```

**Ожидаемый результат:** список из трёх позиций, включая `Кроссовки Sprint`, `Футболка Run` и `Мяч Match`.

## 2. Поиск товара

```python
from src.catalog import search_advanced
from src.storage import load_products

products = load_products("data/products.json")
matches = search_advanced(products, "кроссовки", category="Обувь", max_price=5000)
print([product["name"] for product in matches])
```

**Ожидаемый результат:** `['Кроссовки Sprint']`.

## 3. Добавление в корзину

```python
from src.cart import add_to_cart
from src.storage import load_products

products = load_products("data/products.json")
cart = []
ok, message = add_to_cart(cart, products, 1, 40, 2)
print(ok, message, cart)
```

**Ожидаемый результат:** `True`, сообщение `Товар добавлен в корзину`, в корзине одна позиция `Кроссовки Sprint`, размер 40, количество 2.

## 4. Оформление заказа

```python
from src.cart import add_to_cart
from src.orders import create_order, print_order
from src.storage import load_products

products = load_products("data/products.json")
cart = []
add_to_cart(cart, products, 1, 40, 2)
order = create_order(cart, "Имя клиента", products)
print_order(order)
```

**Ожидаемый результат:** вывод заказа для указанного клиента с двумя парами кроссовок и итогом `9000.00`.

## 5. Просмотр аналитики

```python
from src.analytics import average_order_total, best_selling_product, total_revenue

orders = [{"total": 9000, "items": [{"name": "Кроссовки Sprint", "quantity": 2}]}]
print(total_revenue(orders))
print(best_selling_product(orders))
print(average_order_total(orders))
```

**Ожидаемый результат:** выручка `9000.0`, лучший товар `Кроссовки Sprint`, средний чек `9000.0`.

## 6. Сохранение и загрузка заказов

```python
from src.orders import load_orders, save_orders

save_orders([order], "data/orders.json")
orders = load_orders("data/orders.json")
print(len(orders), orders[0]["total"])
```

**Ожидаемый результат:** `1 9000.0`. `order` — заказ, созданный в предыдущем примере. Файл сохраняется в `data/orders.json`.

## Быстрый демонстрационный запуск

```bash
python main.py
```

Программа загрузит каталог, покажет товар с низким остатком, выполнит поиск, добавит товар в корзину и выведет демонстрационный заказ.
