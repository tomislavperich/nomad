import os
import shutil
from pathlib import Path

from .factory import DotfileHandlerFactory


class DotfileHandler:
    """Manages dotfile.

    Operates on dotfile loaded from config file.

    Attribs:
        path: Path to dotfile.
    """

    def __init__(self, path: str):
        """Initializes Dotfile class."""
        self.path = path
        self.absolute_path = self._resolve_path(path)
        self.path_type = self._get_path_type(self.absolute_path)

        factory = DotfileHandlerFactory()
        self.dotfile_handler = factory.get_handler(self.path_type)

    def _resolve_path(self, path: str) -> Path:
        """Resolves given path to absolute.

        Args:
            path: Path to be resolved.

        Returns:
            Returns resolved, absolute Path object.
        """
        if path.startswith("~"):
            return Path(path).expanduser()

        return Path(path).absolute()

    def _get_path_type(self, path: Path) -> str:
        """Determines path type.

        Determines whether the path is a file or a directory.

        Args:
            path: Path to the dotfile.

        Returns:
            Returns a string indicating path type.
        """
        if path.is_dir():
            return 'dir'
        elif path.is_file():
            return 'file'

        return 'unknown'

    # ? Maybe rename these two methods to fetch/push
    def update(self) -> None:
        """Fetches dotfiles from given path"""
        self.dotfile_handler.update(self.absolute_path)

    def bootstrap(self) -> None:
        """Bootstraps dotfiles to given path."""
        self.dotfile_handler.bootstrap(self.absolute_path)
