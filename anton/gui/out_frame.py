"""Outside League Anton Window

This module contains the implementation of the outside league
anton GUI using customtkinter and `root_gui.py`'s RootGui
"""

from typing import Optional, Tuple, Union, Any
from customtkinter import CTkFrame, CTkLabel, CTk, CTkOptionMenu
from tkinter import Menu, Variable
from config_manager import ConfigManager

class OutFrame(CTkFrame):
    """Outside League Anton Window
    
    This is an implementation of a customtkinter frame to make the 
    GUI of outside league anton window, it uses `customtkinter.CtkFrame`

    It is supposed to be used with root_gui's Ctk Implementation as it's master,
    but it can, theoritcally be used with any Ctk Class
    """

    master: CTk

    def __init__(self, master: CTk, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        """Initialize Outside League Frame"""
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.master = master

        master.title("Outside Anton")
        self.set_geometry("400x600")

        self.pack()

    def make(self) -> None:        
        """Makes the GUI of Outside league window"""
        
        # Navbar
        menu = Menu(master=self)
        self.master.config(menu=menu)
        
        # Preferences
        def hide_to_tray_save() -> bool:
            """Helper function to toggle `hide_to_tray` and save config
            
            Returns:
                bool: flag of sucesseful save
            """
            ConfigManager.preferences.toggle_hide_to_tray()
            hide_to_tray_from_config.get()
            return ConfigManager.preferences.save()
        
        preferences = Menu(menu, tearoff=False)
        hide_to_tray_value = ConfigManager.preferences.hide_to_tray
        hide_to_tray_from_config = Variable(menu, int(ConfigManager.preferences.hide_to_tray))
        hide_to_tray_from_config.set(hide_to_tray_value)
        preferences.add_checkbutton(label='Hide To Tray', command=hide_to_tray_save, variable=hide_to_tray_from_config)
        menu.add_cascade(label='Preferences', menu=preferences)        
           
        label1 = CTkLabel(master=self, text="Test")
        label1.pack()
    
    def set_geometry(self, geometry:str) -> None:
        """Sets geometry of the window
        
        This is function is a custom implementation of how 
        geometry works in `OutFrame`, the window will have a geometry of `x`,
        and will not be able to be resized
        
        Raises:
            ValueError: if geometry is invalid
        """
        if geometry is None or not isinstance(geometry, str):
            raise ValueError("OutFrame.set_geometry took an invalid argument(geometry)")
        
        self.master.geometry(geometry)

        width, height = (int(x) for x in geometry.split("x"))
        self.master.maxsize(width, height)
        self.master.minsize(width, height)