"""Entry-Point

Initializes Configs
"""

import sys
from anton.constants import EXIT_CODE_OK
from anton.gui.root_gui import RootGui
from anton.gui.out_frame import OutFrame
from anton.config_manager import ConfigManager


def main() -> int:
    """Anton Entry-Point"""
    gui = RootGui()
    out_frame = OutFrame(gui)
    out_frame.make()
    gui.mainloop()
    return EXIT_CODE_OK


if __name__ == "__main__":
    sys.exit(main())
