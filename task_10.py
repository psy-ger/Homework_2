
from typing import Callable, Dict, Any, Tuple


def create_product(name: str, price: float, quantity: int) -> Tuple[Callable[[float], str], Callable[[], Dict[str, Any]]]:
    """create_product function that returns functions to set price and get product info"""
    def set_price(new_price: float) -> str:
        """set_price function to update the product price"""
        nonlocal price
        price = new_price
        return f"Ціна товару '{name}' змінена на {price}"

    def get_info() -> Dict[str, Any]:
        """get_info function to retrieve product information"""
        return {
            'name': name,
            'price': price,
            'quantity': quantity
        }
    return set_price, get_info


# my_example_usage
set_price: Callable[[float], str]
get_info: Callable[[], Dict[str, Any]]
set_price, get_info = create_product('Ноутбук', 25000, 5)
print(get_info())
print(set_price(23000))
print(get_info())
