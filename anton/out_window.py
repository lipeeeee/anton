"""Implemetation of the anton outside league window

Will have outside league functionalities such as:
1. Status Manipulation(Offline and status message).
2. Clear Challenges
3. ...
"""

from tkinter import *
from window import Window

class OutWindow(Window):
    """Outside League Window Implementation
    
    """

    # Tkinter.Tk atributes https://docs.python.org/3/library/tkinter.html#tkinter.Tk
    screen_name: str | None
    base_name: str | None
    class_name: str
    use_tk: bool
    sync: bool
    use: str | None

    # Window is visible flag
    visible: bool

    def __init__(self, screen_name: str | None = None, base_name: str | None = None, 
                class_name: str = "OUTSIDE ANTON", use_tk: bool = True, sync: bool = False, use: str | None = None) -> None:
        
        # Automatically sets Window atributes:
        super().__init__(screen_name, base_name, class_name, use_tk, sync, use)

    def make(self) -> None:
        """Custom make for the outside window anton
        
        """

        # Navbar
        menu = Menu(self)
        self.config(menu=menu)

        preferences = Menu(menu, tearoff=False)
        preferences.add_command(label="Hide To Tray", command={})
        menu.add_cascade(label='Preferences', menu=preferences)

        # 

        self.mainloop()