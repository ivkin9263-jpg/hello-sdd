# Hello Function — Specification

## Описание
Функция `greet()` принимает имя пользователя и возвращает приветствие.

## Интерфейс
- **Вход:** `greet(name: str) -> str`
- **Выход:** строка вида `"Hello, {name}!"`

## Краевые случаи / Ошибки
- Если `name` — пустая строка → возвращается `"Hello, World!"`
- Если `name` — `None` → выбрасывается `ValueError("Name cannot be None")`
- Если `name` — не строка → выбрасывается `TypeError("Name must be a string")`
- Имя обрезается по краям (strip)

## Критерии приемки (Acceptance Criteria)
1. `greet("Alice")` → `"Hello, Alice!"`
2. `greet("")` → `"Hello, World!"`
3. `greet("  Bob  ")` → `"Hello, Bob!"`
4. `greet(None)` → `ValueError`
5. `greet(42)` → `TypeError`