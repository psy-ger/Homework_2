
from typing import Dict, Any, Tuple, Callable


def create_user_settings() -> Tuple[Callable[[str, Any], str], Callable[[str], Any], Callable[[], Dict[str, Any]]]:
    """create_user_settings function to manage user settings with nested functions"""
    settings: Dict[str, Any] = {
        'theme': 'light',
        'language': 'uk',
        'notifications': True
    }

    def set_setting(key: str, value: Any) -> str:
        """set_setting function to update a setting"""
        if key in settings:
            settings[key] = value  # update the setting
            return f"Налаштування '{key}' змінено на {value}"
        else:
            return f"Параметр '{key}' не знайдено"

    def get_setting(key: str) -> Any:
        """get_setting function to retrieve a setting"""
        return settings.get(key, f"Параметр '{key}' не знайдено")

    def view_settings() -> Dict[str, Any]:
        """view_settings function to view all settings"""
        return settings.copy()

    return set_setting, get_setting, view_settings


# example usage
set_setting: Callable[[str, Any], str]
get_setting: Callable[[str], Any]
view_settings: Callable[[], Dict[str, Any]]
set_setting, get_setting, view_settings = create_user_settings()
print(view_settings())
print(set_setting('theme', 'dark'))
print(set_setting('language', 'en'))
print(set_setting('notifications', False))
print(view_settings())
print(get_setting('theme'))
print(get_setting('timezone'))  # non-existent setting
