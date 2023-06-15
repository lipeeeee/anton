"""Entry-Point

"""

import sys
from constants import EXIT_CODE_OK
from out_window import OutWindow
import config
import keyboard

def main() -> int:
    """Anton Entry-Point"""
    wnd = OutWindow()
    keyboard.on_press_key("F5", lambda _:wnd.toggle_show())
    wnd.make()
    print(wnd)

    return EXIT_CODE_OK

if __name__ == "__main__":
    sys.exit(main())