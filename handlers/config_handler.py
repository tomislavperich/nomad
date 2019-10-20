import os

import yaml


class ConfigHandler:
    """Manages config files.

    Manages configuration files. Takes care of loading and more.

    Attributes:
        path: A string indicating the path of the config file to use
    """

    def __init__(self, path: str = ""):
        """Initializes Config class with config"""
        self.config = self.load(path)

    def load(self, path: str) -> dict:
        """Loads config file from path.

        If the default path isn't passed in, it looks in default
        config directories.

        Args:
            path: Path to the config file.

        Returns:
            A dictionary containing config file's data.
        """
        data: dict = {}

        if os.path.isfile(path):
            with open(path, "r") as stream:
                try:
                    data = yaml.safe_load(stream)
                except yaml.YAMLError as e:
                    print(f"[!] Error: {e}")

        return data

    def print(self):
        """Prints config file contents."""
        print(yaml.safe_dump(self.config))
