"""Base config class for each of anton's configs

This module contains the base class for each config respectivelly:

preferences.json: 
    - Hide to tray (bool)

"""

from __future__ import annotations
import os
from pathlib import Path

class Config:
    """Base class for the various configurations in anton
    
    Attributes
        - name(str): the specific name of the config
        - config_folder(str): the path to the home directory config folder
        - config_file(str): the path to the specific config json
        
    Has features such as:
        - `load()` to load the specific config from disk
        - `save()` to save the contents of the config into disk
        - `defaults()` load defaults for specific config

    And Utility functions such as:
        - `config_folder_exists()`
        - `create_config_folder()`
        - `config_file_exists()`
    """

    name: str
    config_folder: str
    config_file: str

    def __init__(self, name: str | None = None) -> None:
        """Initialize Config Utility
        
        Raises:
            AssertionError if name is `None`
        
        Returns:
            `self@Config` after initialization
        """
        assert name is not None

        self.name = name
        self.config_folder = str(Path.home()) + "/anton/"
        self.config_file = self.config_folder + name + ".json"

    def load(self) -> bool:
        """Loads config from disk
        
        Raises:
            NotImplementedError

        Returns:
            flag(bool) to know if config was sucessefuly loaded
        """
        raise NotImplementedError("Config.load not implemented")
    
    def save(self) -> bool:
        """Saves config to disk
        
        Raises:
            NotImplementedError

        Returns:
            flag(bool) to know if config was sucessefuly saved
        """
        raise NotImplementedError("Config.save not implemented")
    
    def defaults(self) -> None:
        """Sets atributes to their default values
        
        Raises:
            NotImplementedError
        """
        raise NotImplementedError("Config.defaults not implemented")        

    def config_folder_exists(self) -> bool:
        """Checks if there is an `anton/` folder in home directory
        
        Returns:
            flag(bool) of if there was a config folder before creation
        """
        config_exists = os.path.exists(self.config_folder)

        return config_exists

    def create_config_folder(self) -> None:
        """Creates config folder in home directory

        Raises:
            AssertionError if couldnt retrieve `config_folder` path 
            or folder already exists
        """
        assert self.config_folder and not self.config_folder_exists()
        return os.mkdir(self.config_folder)

    def config_file_exists(self) -> bool:
        """Checks if the configuration file is present on disk
        
        Returns:
            flag(bool) of if the config file exists or not(bool)
        """
        return os.path.exists(self.config_file)
    
    def create_config_file(self) -> bool:
        """Creates default config file in `config_folder`
        
        Generates new config file in home directory with default values
        
        Raises:
            AssertionError if couldnt retrieve `config_file` path
            or file already exists or config folder doesnt exist
        
        Returns:
            flag(bool) if everything was done well
        """
        assert self.config_file and not self.config_file_exists() and self.config_folder_exists()
        self.defaults()
        return self.save()