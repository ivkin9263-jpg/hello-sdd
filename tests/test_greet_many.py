"""Tests for the greet_many function."""

import pytest

from src.hello import greet_many


def test_greet_many_two_names():
    """greet_many(["Alice", "Bob"]) should return "Hello, Alice and Bob!"."""
    assert greet_many(["Alice", "Bob"]) == "Hello, Alice and Bob!"


def test_greet_many_one_name():
    """greet_many(["Alice"]) should return "Hello, Alice!"."""
    assert greet_many(["Alice"]) == "Hello, Alice!"


def test_greet_many_empty_list():
    """greet_many([]) should return "Hello, World!"."""
    assert greet_many([]) == "Hello, World!"


def test_greet_many_none_raises_value_error():
    """greet_many(None) should raise ValueError."""
    with pytest.raises(ValueError, match="Names cannot be None"):
        greet_many(None)


def test_greet_many_non_string_raises_type_error():
    """greet_many([42]) should raise TypeError."""
    with pytest.raises(TypeError, match="Each name must be a string"):
        greet_many([42])


def test_greet_many_stripped_names():
    """greet_many(["  Bob  ", "  Alice  "]) should return "Hello, Bob and Alice!"."""
    assert greet_many(["  Bob  ", "  Alice  "]) == "Hello, Bob and Alice!"
