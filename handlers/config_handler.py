import os

import yaml


class ConfigHandler():
    """Manages config files.

    Manages configuration files. Takes care of loading and more.

    Attributes:
        path: A string indicating the path of the config file to use.
        profile: Profile to use.
    """

    def __init__(self, path: str = "", profile_name: str = ""):
        """Initializes Config class with config"""
        self.profile = profile_name
        self.config = self._try_load(path)
        self.paths = self.get_paths(self.config, self.profile)

    # TODO: Move loading logic outside class
    def _try_load(self, path: str) -> dict:
        try:
            return self.load(path)
        except FileNotFoundError as e:
            print(f"[!] File '{path}' hasn't been found")
            exit(1)

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

    def get_paths(self, config: dict, profile: str = "") -> list:
        """Gets list of paths from config.

        Retrieves a list of dotfile paths from config.

        Args:
            config: Config dict with dotfile paths.
            profile: Optional profile to take from config.

        Returns:
            list: List of paths from config.
        """
        if profile:
            print(f"[i] Using profile {profile}")
            return self._get_profile_paths(config, profile)

        print(f"[i] Using all profiles")
        return self._get_all_paths(config)

    def _get_profile_paths(self, config, profile_name) -> list:
        """Gets list of paths for a single profile."""
        profile = self.config[profile_name]
        return profile["dotfiles"]

    def _get_all_paths(self, config: dict) -> list:
        """Gets all paths from a config."""
        keys = list(config.keys())
        paths = []
        for key in keys:
            for path in config[key]["dotfiles"]:
                paths.append(path)

        return paths

    def format_config(self):
        """Formats config file contents for printing."""
        return yaml.safe_dump(self.config)

    def print_config(self):
        """Prints formatted config"""
        print(self.format_config())
