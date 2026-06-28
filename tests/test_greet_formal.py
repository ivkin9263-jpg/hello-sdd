"""Tests for the greet_formal function."""

import pytest

from src.hello import greet_formal


def test_greet_formal_with_title():
    """greet_formal("Mr.", "Smith") should return "Hello, Mr. Smith!"."""
    assert greet_formal("Mr.", "Smith") == "Hello, Mr. Smith!"


def test_greet_formal_strips_name():
    """greet_formal("Dr.", " Watson") should return "Hello, Dr. Watson!"."""
    assert greet_formal("Dr.", " Watson") == "Hello, Dr. Watson!"


def test_greet_formal_empty_title():
    """greet_formal("", "Alice") should return "Hello, Alice!"."""
    assert greet_formal("", "Alice") == "Hello, Alice!"


def test_greet_formal_none_raises_value_error():
    """greet_formal("Prof.", None) should raise ValueError."""
    with pytest.raises(ValueError, match="Name cannot be None"):
        greet_formal("Prof.", None)


def test_greet_formal_non_string_raises_type_error():
    """greet_formal("Mr.", 42) should raise TypeError."""
    with pytest.raises(TypeError, match="Name must be a string"):
        greet_formal("Mr.", 42)
