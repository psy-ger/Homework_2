
from typing import List

subscribers: List[str] = []  # list to store subscriber names


def subscribe(name: str) -> str:
    """subscribe(name) - add a new subscriber and return a confirmation message."""
    subscribers.append(name)

    def confirm_subscription() -> str:
        """confirm_subscription() - return a confirmation message."""
        return f"Підписка підтверджена для {name}"
    return confirm_subscription()


def unsubscribe(name: str) -> str:
    """unsubscribe(name) - remove a subscriber and return a confirmation message."""
    if name in subscribers:
        subscribers.remove(name)
        return f"{name} успішно відписаний"
    else:
        return f"Підписник {name} не знайдений"


subscribe("Олена")
subscribe("Ігор")
print(subscribers)  # ['Олена', 'Ігор']
print(unsubscribe("Ігор"))  # 'Ігор успішно відписаний'
print(subscribers)  # ['Олена']
