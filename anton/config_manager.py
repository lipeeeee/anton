"""Config Manager

Encompasses every config used in anton
"""

from configs.preferences import Preferences

class ConfigManager():
    """**STATIC** Config Manager for anton
    
    Has all anton configs such as:
        Preferences(Config)

    Usage: 
    ```py
    >> from config_manager import ConfigManager

    >> # Get Hide_To_Tray attribute from preferences config
    >> print(ConfigManager.preferences.hide_to_tray)
    ```

    Raises:
        TypeError if trying to initialize it
    """

    # Configs
    preferences: Preferences = Preferences()

    def __init__(self) -> None:
        raise TypeError("Cannot Initialize Config Manager because it is a static class")
    
    def __new__(cls) -> None:
        raise TypeError("Cannot Initialize Config Manager because it is a static class")