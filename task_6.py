
def create_calculator(operator):
    """create_calculator function that returns a calculator function based on the operator"""
    def calculator(a, b):
        """calculator function to perform the operation"""
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                return 'Ділення на нуль неможливе'
            return a / b
        else:
            return 'Невідомий оператор'
    return calculator


add = create_calculator('+')
subtract = create_calculator('-')
multiply = create_calculator('*')
divide = create_calculator('/')

print(add(10, 5))        # 15
print(subtract(10, 5))   # 5
print(multiply(10, 5))   # 50
print(divide(10, 5))     # 2.0
print(divide(10, 0))     # 'Ділення на нуль неможливе'
