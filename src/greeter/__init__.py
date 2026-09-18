def greet(name: str, punctuation: bool = True) -> str:
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    if not name.strip():
        raise ValueError("name must not be empty or whitespace-only")
    if not isinstance(punctuation, bool):
        raise TypeError("punctuation must be a boolean")
    suffix = "!!!" if punctuation else ""
    return f"Hello, {name}{suffix}"
