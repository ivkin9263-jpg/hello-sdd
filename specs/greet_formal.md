# greet_formal — Specification

## Описание
Функция `greet_formal()` принимает обращение (титул) и имя, возвращает формальное приветствие.

## Интерфейс
**Вход:** `greet_formal(title: str, name: str) -> str`

## Примеры
- `greet_formal("Mr.", "Smith")` → `"Hello, Mr. Smith!"`
- `greet_formal("Dr.", " Watson")` → `"Hello, Dr. Watson!"` (имя обрезается)
- `greet_formal("", "Alice")` → `"Hello, Alice!"` (без титула)
- `greet_formal("Prof.", None)` → `ValueError`
- `greet_formal("Mr.", 42)` → `TypeError`