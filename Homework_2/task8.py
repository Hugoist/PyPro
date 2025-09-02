from typing import Callable, Any, Optional


def create_user_settings() -> Callable[[str, Optional[Any]], None]:
    """Return function to store, update, and view user settings."""

    settings: dict[str, Any] = {
        "theme": "dark",
        "language": "uk",
        "notifications": True
    }

    def manage_settings(key: str, value: Optional[Any] = None) -> None:
        """Set or view a setting"""
        if key not in settings:
            print(f"Невідомий параметр '{key}'")
            return

        if value is not None:
            settings[key] = value
            print(f"Параметр '{key}' оновлено на: '{value}'")
        else:
            print(f"{key}: {settings[key]}")

    return manage_settings


user_settings = create_user_settings()

user_settings("theme")  # theme: light
user_settings("theme", "light")  # Параметр 'theme' оновлено на: 'light'
user_settings("theme")  # theme: dark
user_settings("notifications")  # notifications: True
user_settings("notifications", False)
user_settings("notifications")  # notifications: False
user_settings("zoom")  # Невідомий параметр 'zoom'
