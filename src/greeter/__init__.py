def greet(
    name: str, punctuation: bool = True, capitalized: bool = False
) -> str:
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    if not name.strip():
        raise ValueError("name must not be empty or whitespace-only")
    if not isinstance(punctuation, bool):
        raise TypeError("punctuation must be a boolean")
    if not isinstance(capitalized, bool):
        raise TypeError("capitalized must be a boolean")
    if capitalized:
        leading_whitespace = name[: len(name) - len(name.lstrip())]
        name_start = len(leading_whitespace)
        displayed_name = (
            leading_whitespace
            + name[name_start : name_start + 1].upper()
            + name[name_start + 1 :]
        )
    else:
        displayed_name = name
    suffix = "!!!" if punctuation else ""
    return f"Hello, {displayed_name}{suffix}"
