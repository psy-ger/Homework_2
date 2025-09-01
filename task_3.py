discount = 0.1  # global discount of 10%


def create_order(price):
    """create_order function with nested apply_additional_discount function"""
    final_price = price * (1 - discount)  # apply global discount
    print(f"Ціна після глобальної знижки: {final_price}")

    def apply_additional_discount(additional):
        """apply_additional_discount function to apply an additional discount"""
        nonlocal final_price
        final_price *= (1 - additional)  # apply additional discount
        print(f"Ціна після додаткової знижки: {final_price}")
    return final_price, apply_additional_discount


order_price, add_discount = create_order(1000)
add_discount(0.05)  # additional 5% discount
# final price without additional discount applied
print(f"Фінальна ціна: {order_price}")
