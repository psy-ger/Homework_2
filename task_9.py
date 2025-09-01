
from typing import Callable, Any, Dict, Tuple


def memoize(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to cache function results."""
    cache: Dict[Tuple[Any, ...], Any] = {}

    def wrapper(*args: Any) -> Any:
        """Wrapper function to check cache before calling the original function."""
        if args in cache:
            print(f"Взято з кешу: {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@memoize
def factorial(n: int) -> int:
    """Calculate factorial of n with memoization."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # 120
print(factorial(6))  # 720
