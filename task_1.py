import builtins


def my_sum(iterable):
    """Custom sum function that mimics the built-in sum function"""
    print(f"This is my custom sum function!")


list_numbers = [1, 2, 3, 4, 5]

print(f"Sum of list_diggit: {sum(list_numbers)}")
my_sum(list_numbers)
sum = my_sum
sum(list_numbers)
