"""Tests for the greet function."""

import pytest

from src.hello import greet


def test_greet_normal_name():
    """greet("Alice") should return "Hello, Alice!"."""
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty_string():
    """greet("") should return "Hello, World!"."""
    assert greet("") == "Hello, World!"


def test_greet_stripped_name():
    """greet("  Bob  ") should return "Hello, Bob!"."""
    assert greet("  Bob  ") == "Hello, Bob!"


def test_greet_none_raises_value_error():
    """greet(None) should raise ValueError."""
    with pytest.raises(ValueError, match="Name cannot be None"):
        greet(None)


def test_greet_non_string_raises_type_error():
    """greet(42) should raise TypeError."""
    with pytest.raises(TypeError, match="Name must be a string"):
        greet(42)
