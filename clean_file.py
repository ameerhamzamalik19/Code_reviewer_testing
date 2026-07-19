from typing import Optional

def add(a: int, b: int) -> int:
    return a + b

def greet(name: Optional[str]) -> str:
    return name or "Guest"