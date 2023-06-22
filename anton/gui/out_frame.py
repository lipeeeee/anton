"""Outside League Anton Window

This module contains the implementation of the outside league
anton GUI using customtkinter and `root_gui.py`'s RootGui
"""

from typing import Optional, Tuple, Union, Any
from customtkinter import CTkFrame, CTkLabel, CTk

class OutFrame(CTkFrame):
    """Outside League Anton Window
    
    This is an implementation of a customtkinter frame to make the 
    GUI of outside league anton window, it uses `customtkinter.CtkFrame`

    It is supposed to be used with root_gui's Ctk Implementation as it's master,
    but it can, theoritcally be used with any Ctk Class
    """

    def __init__(self, master: CTk, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        """Initialize Outside League Frame"""
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        master.title("Outside Anton")
        master.geometry("400x600")

        self.pack()

    def make(self) -> None:        
        """Makes the GUI of Outside league window"""
        label1 = CTkLabel(master=self, text="Test")
        label1.pack()