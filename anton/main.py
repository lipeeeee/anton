"""Entry-Point

Initializes Configs
"""

import sys
from constants import EXIT_CODE_OK
from gui.root_gui import RootGui
from gui.out_frame import OutFrame
from config_manager import ConfigManager
import keyboard

def main() -> int:
    """Anton Entry-Point"""
    gui = RootGui()
    out_frame = OutFrame(gui)
    out_frame.make()
    gui.mainloop()
    return EXIT_CODE_OK

if __name__ == "__main__":
    sys.exit(main())