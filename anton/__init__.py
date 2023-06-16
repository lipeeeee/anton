"""Anton Library

Includes:
- Windows classes
    - Window(base class)
    - OutWindow
    - InWindow

- Config Classes
    - ConfigManager
    - Preferences
"""

from .constants import EXIT_CODE_OK, EXIT_CODE_BAD
from .main import main 

# Windows
from .window import Window
from .out_window import OutWindow

# Configs
from .config_manager import ConfigManager
from .configs.config import Config
from .configs.preferences import Preferences