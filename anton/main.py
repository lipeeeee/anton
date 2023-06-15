"""
    Entry-Point
"""

import sys
from constants import EXIT_CODE_OK
from window import Window
import keyboard

def main() -> int:
    """Anton Entry-Point"""
    wnd = Window()
    keyboard.on_press_key("F5", lambda _:wnd.toggle_show())
    wnd.make(topmost=True)
    print(wnd)

    return EXIT_CODE_OK

if __name__ == "__main__":
    sys.exit(main())