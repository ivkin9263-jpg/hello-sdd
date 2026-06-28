# greet_many — Specification

## Описание
Функция `greet_many()` принимает список имён и возвращает приветствие.

## Интерфейс
**Вход:** `greet_many(names: list[str] | None = None) -> str`

**Выход:** строка-приветствие.

## Краевые случаи
- `names = ["Alice", "Bob"]` → `"Hello, Alice and Bob!"`
- `names = ["Alice"]` → `"Hello, Alice!"`
- `names = []` → `"Hello, World!"`
- `names = None` → `ValueError("Names cannot be None")`
- Элемент списка — не строка → `TypeError("Each name must be a string")`
- Имена обрезаются по краям (strip)

## Критерии приемки
1. `greet_many(["Alice", "Bob"])` → `"Hello, Alice and Bob!"`
2. `greet_many(["Alice"])` → `"Hello, Alice!"`
3. `greet_many([])` → `"Hello, World!"`
4. `greet_many(None)` → `ValueError`
5. `greet_many([42])` → `TypeError`
6. `greet_many(["  Bob  ", "  Alice  "])` → `"Hello, Bob and Alice!"`