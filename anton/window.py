"""Base Anton GUI

Contains `Window` class that 
can be inherited to implement INGAME and OUTGAME windows,
represents a Tkinter.Tk Object

# Example
```py
>> from window import Window

>> # Initialize object
>> wnd = Window()

>> # Create window and show it
>> wnd.make(topmost=True)

>> # String representation of window
>> print(wnd)
WINDOW {
        screen_name: 'None',
        base_name: 'None',
        class_name: 'TK_Window',
        use_tk: 'True',
        sync: 'False',
        use: 'None',
        visible: 'True'
}
```"""

from tkinter import *
from tkinter import ttk
from typing import Any

class Window(Tk):
    """Tkinter Inherited GUI"""

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
                class_name: str = "TK_Window", use_tk: bool = True, sync: bool = False, use: str | None = None) -> None:
        self.screen_name = screen_name
        self.base_name = base_name
        self.class_name = class_name
        self.use_tk = use_tk
        self.sync = sync
        self.use = use
        self.visible = False # Not yet created

        return super().__init__(screen_name, base_name, class_name, use_tk, sync, use)

    def __str__(self) -> str:
        builder: str = "WINDOW { \n"
        builder += f"\tscreen_name: '{self.screen_name}',\n"
        builder += f"\tbase_name: '{self.base_name}',\n"
        builder += f"\tclass_name: '{self.class_name}',\n"
        builder += f"\tuse_tk: '{self.use_tk}',\n"
        builder += f"\tsync: '{self.sync}',\n"
        builder += f"\tuse: '{self.use}',\n"
        builder += f"\tvisible: '{self.visible}'\n"
        builder += "};"
        return builder

    def __repr__(self) -> str:
        return str(self)

    def make(self) -> None:
        """Creates window
        
        Raises:
            NotImplementedError
        """
        raise NotImplementedError("window.Make is not implemented")

    def hide(self) -> None:
        """Hide window"""
        self.visible = False
        return self.withdraw()

    def show(self) -> None:
        """Show Window"""
        self.visible = True
        return self.deiconify()

    def toggle_show(self) -> None:
        """Toggles between hid and shown"""
        print("toggle")
        if not self.visible:
            return self.show()
        return self.hide()

    def set_atribute(self, option: str, value: Any) -> None:
        """Set Atribute of self(Tk) object
        
        Args:
            option (str): Atribute to edit.
            value (Any): Value to edit the atribute with.
        """
        return self.attributes(option, value)