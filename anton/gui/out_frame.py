"""Outside League Anton Window

This module contains the implementation of the outside league
anton GUI using customtkinter and `root_gui.py`'s RootGui
"""

from typing import Optional, Tuple, Union, Any
from customtkinter import CTkFrame, CTkLabel

class OutFrame(CTkFrame):
    """Outside League Anton Window
    
    This is an implementation of a customtkinter frame to make the 
    GUI of outside league anton window, it uses `customtkinter.CtkFrame`

    It is supposed to be used with root_gui's Ctk Implementation as it's master,
    but it can, theoritcally be used with any Ctk Class
    """

    def __init__(self, master: Any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
    
    def make(self) -> None:
        """Makes the GUI of Outside league window"""
        label1 = CTkLabel(master=self, text="Test", width=50, height=100)
        label1.pack()