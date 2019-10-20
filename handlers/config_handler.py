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
        try:
            self.config = self.load(path)
        except FileNotFoundError as e:
            print(f"[!] File '{path}' hasn't been found")

    def load(self, path: str) -> dict:
        """Loads config file from path.

        If the default path isn't passed in, it looks in default
        config directories.

        Args:
            path: Path to the config file.

        Returns:
            A dictionary containing config file's data.

        Raises:
            FileNotFoundError: If config file is not found.
        """
        data: dict = {}

        if os.path.isfile(path):
            with open(path, "r") as stream:
                try:
                    data = yaml.safe_load(stream)
                except yaml.YAMLError as e:
                    print(f"[!] Error: {e}")
        else:
            raise FileNotFoundError(f"File {path} not found")

        return data

    def print(self):
        """Prints config file contents."""
        print(yaml.safe_dump(self.config))
