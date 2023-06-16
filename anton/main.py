"""Entry-Point

"""

import sys
from constants import EXIT_CODE_OK
from out_window import OutWindow
from configs.preferences import Preferences
import keyboard

def main() -> int:
    """Anton Entry-Point"""
    wnd = OutWindow()
    a = Preferences()
    
    keyboard.on_press_key("F5", lambda _:wnd.toggle_show())
    wnd.make()
    print(wnd)

    return EXIT_CODE_OK

if __name__ == "__main__":
    sys.exit(main())