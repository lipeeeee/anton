"""RootGui Module

This module contains a custom implementation of `customtkinter.CTk`
that will later be used on frame creation

Q: Should the rootgui be static?
A: Probably not, more refactoring todo
"""

from typing import Tuple
from customtkinter import CTk, set_appearance_mode, set_default_color_theme

class RootGui(CTk):
    """RootGui Class
    
    Custom Implementation of `customtkinter.CTk` to fit anton's requirements.   
    This will be the root that is passed through the creation of outside and inside
    league frames.

    Attributes:
        _geometry (str): the resolution of the window in a str format, eg: "100x100"
    """

    _geometry: str 

    # Functions from customtkinter
    _set_appearence_mode = set_appearance_mode
    _set_default_color_theme = set_default_color_theme

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs) -> None:
        """Initializes `customtkinter` and `customtkinter.CTk` with anton's configuration
        
        Configuration changes:
            `appearence_mode`: Color Scheme
            `default_color_theme`: Color Theme
        """
        # customtkinter initialization
        set_appearance_mode('system')
        set_default_color_theme('dark-blue')

        # customtikinter.CTk initialization
        super().__init__(fg_color, **kwargs)

    def __str__(self) -> str:
        builder: str = "RootGui(" + str(id(self)) + ") {\n"
        builder += f"\tappearance_mode: '{self._get_appearance_mode()}',\n"
        builder += f"\twindow_scaling: '{str(self._get_window_scaling())}',\n"
        builder += f"\ttitle: '{self.title()}',\n"
        builder += f"\tstate: '{self.state()}',\n"
        builder += f"\tsize: '{str(self.size())}',\n"
        builder += "};"
        return builder

    def __repr__(self) -> str:
        return f"<RootGui {str(id(self))}>"

    def set_geometry(self, geometry:str) -> None:                
        """Sets the Geometry of self(CTk)
        
        Params:
            geometry (str): the resolution in a string format, eg: "100x200"
        
        Raises:
            ValueError: if geometry is None or is not string
        """
        if geometry is None or not isinstance(geometry, str):
            raise ValueError("RootGui.set_geometry took an invalid argument")

        self._geometry = geometry
        self.geometry(geometry)