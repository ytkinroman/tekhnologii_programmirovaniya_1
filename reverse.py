def my_reverse(value: str) -> str:
    """Отражает строку в обратном порядке."""
    if not value:
        return ""
    if len(value) == 1:
        return value
    if len(value) == 2:
        return f"{value[1]}{value[0]}"
    return my_reverse(value[1:]) + value[0]
