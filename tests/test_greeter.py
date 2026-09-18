import pytest

from greeter import greet


def test_greet_adds_excitement():
    assert greet("Ada") == "Hello, Ada!!!"


def test_greet_preserves_surrounding_whitespace():
    assert greet(" Ada ") == "Hello,  Ada !!!"


@pytest.mark.parametrize("name", ["", "   ", "\t\n"])
def test_greet_rejects_empty_or_whitespace_only_names(name):
    with pytest.raises(ValueError, match="must not be empty or whitespace-only"):
        greet(name)


def test_greet_rejects_non_string_names():
    with pytest.raises(TypeError, match="name must be a string"):
        greet(42)
