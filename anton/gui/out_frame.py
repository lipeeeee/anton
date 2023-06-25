"""Outside League Anton Window

This module contains the implementation of the outside league
anton GUI using customtkinter and `root_gui.py`'s RootGui
"""

from typing import Tuple
from anton.anton import Anton
from anton.background_thread import BackgroundThread
from customtkinter import CTkFrame, CTkLabel, CTk, CTkButton, CTkFont
from tkinter import Menu, Variable
from ..config_manager import ConfigManager


class OutFrame(CTkFrame):
    """Outside League Anton Window

    This is an implementation of a customtkinter frame to make the
    GUI of outside league anton window, it uses `customtkinter.CtkFrame`

    It is supposed to be used with root_gui's Ctk Implementation as it's master,
    but it can, theoretically, be used with any Ctk Class

    Attributes:
        master (CTk): parent of self(CTkFrame), usually a RootGui instance
        width (int): width of frame
        height (int): height of frame
        navbar (Menu): the navbar in outframe
        button_challenges (CTkButton): Button for the challenges reset
    """

    master: CTk
    width: int
    height: int

    # Widgets / Controls
    navbar: Menu
    button_challenges: CTkButton

    def __init__(
        self,
        master: CTk,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        **kwargs
    ):
        """Initialize Outside League Frame"""
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs
        )

        self.master = master
        self.master.title("Outside Anton")
        self.set_geometry("400x600")
        self.master.state("zoomed")  # Starts in top-left of main screen

        # Ui Grids
        self.master.grid_rowconfigure(5, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self.pack()

        # anton
        self.anton = Anton()

    def make(self) -> None:
        """Makes the GUI of Outside league window"""

        # Navbar
        self.navbar = self.make_navbar()
        self.master.config(menu=self.navbar)

        bold_font_24 = CTkFont("Arial", 24, weight="bold")

        # LCA Status label
        self.label_status = CTkLabel(
            master=self, text="STATUS", font=CTkFont("Arial", 16, weight="bold")
        )
        self.label_status.grid(row=0, column=0, pady=0)
        # Update label with status thread
        BackgroundThread(
            fn_to_run=self.update_status_label,
            time_between_runs=self.anton.league_client.LISTEN_TIMEOUT,
            daemon=True,
        ).start()

        # Reset Challenges button
        self.button_challenges = CTkButton(
            master=self,
            text="Reset Challenges",
            width=self.width - 10,
            height=50,
            font=bold_font_24,
            command=self.anton.remove_challenges,
        )
        self.button_challenges.grid(row=1, column=0, pady=5)

        # Start league offline
        self.button_start_offline = CTkButton(
            master=self,
            text="Start LoL Offline",
            width=self.width - 10,
            height=50,
            font=bold_font_24,
        )
        self.button_start_offline.grid(row=2, column=0, pady=5)

        # me:)
        self.me_label = CTkLabel(master=self, text="me:)lipeeeee")
        self.me_label.grid(row=4, column=0, pady=300)

    def make_navbar(self) -> Menu:
        """Helper function that makes a tkinter.Menu Navbar

        Makes a menu/Navbar containing:
        - Preferences
        - ...

        Returns:
            tkinter.Menu: Representing the outside league window
            navbar for anton
        """

        # Initialize all menus
        menu = Menu(master=self)
        preferences = Menu(menu, tearoff=False)

        # Preferences
        # Preferences.Hide to tray
        def hide_to_tray_save() -> bool:
            """Helper function to toggle `hide_to_tray` and save config

            Returns:
                bool: flag of sucesseful save
            """
            ConfigManager.preferences.toggle_hide_to_tray()
            self.set_hide_to_tray(hide_to_tray_from_config.get())
            return ConfigManager.preferences.save()

        # Get values from config
        hide_to_tray_value = ConfigManager.preferences.hide_to_tray
        hide_to_tray_from_config = Variable(
            menu, ConfigManager.preferences.hide_to_tray
        )
        hide_to_tray_from_config.set(hide_to_tray_value)
        self.set_hide_to_tray(hide_to_tray_value)
        preferences.add_checkbutton(
            label="Hide To Tray",
            command=hide_to_tray_save,
            variable=hide_to_tray_from_config,
        )

        # Preferences.Always top
        def always_top_save() -> bool:
            """Helper function to toggle `always_top` and save config

            Returns:
                bool: flag of sucesseful save
            """
            ConfigManager.preferences.toggle_always_top()
            self.set_always_top(always_top_from_config.get())
            return ConfigManager.preferences.save()

        # Get values from config
        always_top_value = ConfigManager.preferences.always_top
        always_top_from_config = Variable(menu, ConfigManager.preferences.always_top)
        always_top_from_config.set(always_top_value)
        self.set_always_top(always_top_value)
        preferences.add_checkbutton(
            label="Always on Top",
            command=always_top_save,
            variable=always_top_from_config,
        )

        # Finish Preferences
        menu.add_cascade(label="Preferences", menu=preferences)

        return menu

    def update_status_label(self) -> None:
        """Updates status label with current `LCA` status"""
        if self.anton.league_client.connected:
            self.label_status.configure(
                text="Connected to League", text_color=("green")
            )
        else:
            self.label_status.configure(
                text="Could not detect League", text_color=("red")
            )

    def set_hide_to_tray(self, flag: bool) -> None:
        """Sets the option to always hide to tray

        Assumes that `flag` is an object representing a boolean,
        doesnt care if it is:
        - "1"(str)
        - 1(int)
        - True(bool)

        Params:
            flag (bool): to know if we hide to tray or not
        """
        if isinstance(flag, int):
            flag = bool(flag)
        elif isinstance(flag, str):
            flag = bool(int(flag))

        if flag is True:
            self.master.protocol("WM_DELETE_WINDOW", self.master.iconify)
        else:
            self.master.protocol("WM_DELETE_WINDOW", self.master.destroy)

    def set_always_top(self, flag: bool) -> None:
        """Sets the option to always stay on top

        Assumes that `flag` is an object representing a boolean,
        doesnt care if it is:
        - "1"(str)
        - 1(int)
        - True(bool)

        Params:
            flag (bool): to know if we stay on top or not
        """
        if isinstance(flag, int):
            flag = bool(flag)
        elif isinstance(flag, str):
            flag = bool(int(flag))

        self.master.attributes("-topmost", flag)
        self.master.update()

    def set_geometry(self, geometry: str) -> None:
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

        self.width, self.height = (int(x) for x in geometry.split("x"))
        self.master.maxsize(self.width, self.height)
        self.master.minsize(self.width, self.height)
