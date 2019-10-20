import os
import shutil
from pathlib import Path


class Dotfile:
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
        return Path(path).resolve()

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


class DotfileHandlerFactory:
    def get_handler(self, path_type: str):
        """Gets dotfile handler based on path type

        Args:
            path_type: Type of path whether it was dir or file

        Returns:
            DotfileHandler: Handler for dotfiles
        """
        if path_type == 'file':
            return DotfileFileHandler()
        elif path_type == 'dir':
            return DotfileDirHandler()
        else:
            raise ValueError(f"Unknown path type: {path_type}")


class DotfileHandler:
    def __init__(self):
        pass


class DotfileFileHandler(DotfileHandler):
    def update(self, path: Path) -> None:
        """
        home_path = os.getenv("HOME")
        local_path = path.relative_to(home_path)

        if not local_path.exists():
            local_path.mkdir()

        shutil.copyfile(path, local_path)
        """
        print("Updating dir, hurr durr...")

    def bootstrap(self, path: Path) -> None:
        """
        home_path = os.getenv("HOME")
        remote_path = f"{home_path}/{path}"

        if not remote_path.exists():
            remote_path.mkdir()

        shutil.copyfile(path, remote_path)
        """
        print("Bootstrapping file, hurr durr...")


class DotfileDirHandler(DotfileHandler):
    def update(self, path: str) -> None:
        """
        home_path = os.getenv("HOME")
        local_path = path.relative_to(home_path)

        if not local_path.exists()
            path.mkdir()

        shutil.copy(path, local_path)
        """
        print("Updating dir, hurr durr...")

    def bootstrap(self, path: str) -> None:
        """
        home_path = os.getenv("HOME")
        local_dir = os.getcwd()
        relative_path = path.relative_to(local_dir)
        remote_path = Path(f"{home_path}/{relative_path}")

        if not remote_path.exists():
            remote_path.mkdir()

        shutil.copy(path, remote_path)
        """
        print("Bootstrapping dir, hurr durr...")
