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
