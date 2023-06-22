"""Preferences Specific Config

Stores the preferences config loading, saving and default logics
"""

from .config import Config
import json

class Preferences(Config):
    """Specific `preferences` config based on ``Anton.Config``

    Config Attributes:
        hide_to_tray (bool): Flag to know if minimizes to tray
        always_top (bool): Flag to know if the window stays always on top

    Implements from base class:
        - `load()`
        - `save()`
        - `defaults()`
        - `json_dict()`
    """

    # Config Attributes
    hide_to_tray: bool
    always_top: bool

    def __init__(self, name: str | None = "preferences") -> None:
        assert name == "preferences"
        super().__init__(name)

    @property
    def json_dict(self) -> str:
        """Generates json dict of current configuration

        Returns:
            str: json dictionary as str
        """
        json_dict = {
            "hide_to_tray": self.hide_to_tray,
            "always_top": self.always_top
        }
        return json.dumps(json_dict)

    def load(self) -> bool:
        """Loads config from disk

        Gets the json object from the conf file
        and gets each attribute from it

        Returns:
            bool: to know if config was sucessefuly loaded
        """
        with open(self.config_file, "r") as file:
            # Get json obj
            json_obj = json.load(file)

            # Get Attributes
            self.hide_to_tray = json_obj["hide_to_tray"]
            self.always_top = json_obj["always_top"]

        return True

    def save(self) -> bool:
        """Saves config to disk

        Dumps `self.json_dict` into a folder

        Returns:
            bool: to know if config was sucessefuly saved
        """
        with open(self.config_file, "w") as file:
            file.write(self.json_dict)

        return True

    def defaults(self) -> None:
        """Sets atributes to their default values"""
        self.hide_to_tray = False
        self.always_top = False

    def toggle_hide_to_tray(self) -> bool:
        """Toggles `hide_to_tray` attribute

        Returns: 
            bool: new value of `hide_to_tray`
        """
        self.hide_to_tray = not self.hide_to_tray
        return self.hide_to_tray

    def toggle_always_top(self) -> bool:
        """Toggles `always_top` attribute

        Returns:
            bool: new value of `always_top`
        """
        self.always_top = not self.always_top
        return self.always_top