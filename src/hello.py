"""Functions for greeting users."""



def greet(name: str | None = None) -> str:
    """Return a greeting message.

    Args:
        name: The name to greet. If None or empty, returns "Hello, World!".

    Returns:
        A greeting string.

    Raises:
        ValueError: If name is None.
        TypeError: If name is not a string.
    """
    if name is None:
        raise ValueError("Name cannot be None")
    if not isinstance(name, str):
        raise TypeError("Name must be a string")

    stripped = name.strip()
    if not stripped:
        return "Hello, World!"

    return f"Hello, {stripped}!"


def greet_many(names: list[str] | None = None) -> str:
    """Return a greeting message for multiple names.

    Args:
        names: A list of names to greet. If empty list, returns "Hello, World!".

    Returns:
        A greeting string combining all names with "and".

    Raises:
        ValueError: If names is None.
        TypeError: If any element in names is not a string.
    """
    if names is None:
        raise ValueError("Names cannot be None")

    stripped_names = []
    for name in names:
        if not isinstance(name, str):
            raise TypeError("Each name must be a string")
        stripped_names.append(name.strip())

    if not stripped_names:
        return "Hello, World!"

    if len(stripped_names) == 1:
        return f"Hello, {stripped_names[0]}!"

    return f"Hello, {' and '.join(stripped_names)}!"
