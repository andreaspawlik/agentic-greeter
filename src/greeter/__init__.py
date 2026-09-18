def greet(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    if not name.strip():
        raise ValueError("name must not be empty or whitespace-only")
    return f"Hello, {name}!!!"
