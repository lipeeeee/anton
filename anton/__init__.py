"""Anton Library

Includes:
- Windows classes
    - Window(base class)
    - OutWindow
    - InWindow

- Config Classes
    - Preferences
"""

from .constants import *
from .main import main 

# Windows
from .window import Window
from .out_window import OutWindow

# Configs
from .configs.config import Config
from .configs.preferences import Preferences