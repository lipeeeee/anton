"""Preferences Specific Config 

Stores the preferences config loading, saving and default logics
"""

from .config import Config
import json

class Preferences(Config):
    """Specific `preferences` config based on ``Anton.Config``
    
    Config Attributes:
        hide_to_tray(bool) - Flag to know if minimizes to tray

    Implements from base class:
        - `load()`
        - `save()`
        - `defaults()`
    """

    # Config Attributes
    hide_to_tray: bool

    def __init__(self, name: str | None = "preferences") -> None:
        assert name == "preferences"
        super().__init__(name)

    def load(self) -> bool:
        """Loads config from disk
        
        Gets the json object from t he conf file
        and gets each attribute from it

        Returns:
            flag(bool) to know if config was sucessefuly loaded
        """
        with open(self.config_file, "r") as file:
            # Get json obj
            json_obj = json.load(file)

            # Get Attributes
            self.hide_to_tray = json_obj["hide_to_tray"]

        return True
    
    def save(self) -> bool:
        """Saves config to disk

        Dumps `self.json_dict` into a folder

        Returns:
            flag(bool) to know if config was sucessefuly saved
        """
        with open(self.config_file, "w") as file:
            file.write(self.json_dict)

        return True
    
    @property
    def json_dict(self):
        """Generates json dict of current configuration"""
        json_dict = {
            "hide_to_tray": self.hide_to_tray
        }
        return json.dumps(json_dict)

    def defaults(self) -> None:
        """Sets atributes to their default values"""
        self.hide_to_tray = False

if __name__ == "__main__":
    p = Preferences()