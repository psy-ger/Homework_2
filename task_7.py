
total_expense: float = 0  # global variable to store total expenses


def add_expense(amount: float) -> None:
    """add_expense(amount) - add an expense to the total."""
    global total_expense
    total_expense += amount  # update total expense


def get_expense() -> float:
    """get_expense() - return the total expense."""
    return total_expense


def main() -> None:
    """Main function to interact with the expense tracker."""
    while True:
        print("\nМеню:")
        print("1. Додати витрату")
        print("2. Переглянути загальну суму витрат")
        print("3. Вийти")
        choice: str = input("Виберіть опцію: ")
        if choice == '1':
            try:
                amount: float = float(input("Введіть суму витрати: "))
                add_expense(amount)
                print(f"Витрату {amount} додано.")
            except ValueError:
                print("Некоректна сума!")
        elif choice == '2':
            print(f"Загальна сума витрат: {get_expense()}")
        elif choice == '3':
            print("Вихід з програми.")
            break
        else:
            print("Некоректний вибір!")


if __name__ == "__main__":
    main()
