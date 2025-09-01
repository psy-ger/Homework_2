def create_product(name, price, quantity):
    """create_product function that returns functions to set price and get product info"""
    def set_price(new_price):
        """set_price function to update the product price"""
        nonlocal price
        price = new_price
        return f"Ціна товару '{name}' змінена на {price}"

    def get_info():
        """get_info function to retrieve product information"""
        return {
            'name': name,
            'price': price,
            'quantity': quantity
        }
    return set_price, get_info


# my_example_usage
set_price, get_info = create_product('Ноутбук', 25000, 5)
print(get_info())
print(set_price(23000))
print(get_info())
