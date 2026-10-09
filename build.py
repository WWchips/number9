"""Проверка проекта, тестирование и запуск демонстрационного приложения."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def check_python_version() -> None:
    if sys.version_info < (3, 10):
        print("Требуется Python 3.10+")
        raise SystemExit(1)
    print(f"Python {sys.version_info.major}.{sys.version_info.minor}: OK", flush=True)


def check_data() -> None:
    data_file = ROOT / "data" / "products.json"
    if not data_file.is_file():
        print("Файл данных не найден: data/products.json")
        raise SystemExit(1)
    print("Файл данных data/products.json: OK", flush=True)


def run_tests() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout, end="", flush=True)
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode:
        print("Тесты не прошли!")
        raise SystemExit(result.returncode)


def run_app() -> None:
    result = subprocess.run([sys.executable, "main.py"], cwd=ROOT)
    if result.returncode:
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    check_python_version()
    check_data()
    run_tests()
    run_app()
    print("Сборка успешна!", flush=True)
