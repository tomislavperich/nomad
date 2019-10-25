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
        self.path = Path(path)
        self.local_base = "dotfiles"
        self.absolute = self._get_absolute(self.path)
        self.category = self._get_path_category(self.path)
        self.factory = DotfileHandlerFactory()

    def _get_absolute(self, path: Path) -> Path:
        """Resolves given path to absolute.

        Args:
            path: Path to be resolved.

        Returns:
            Path: resolved, absolute Path.
        """
        return path.expanduser().absolute()

    def _get_path_type(self, path: Path) -> str:
        """Determines path type.

        Determines whether the path is a file or a directory.

        Args:
            path: Path to the dotfile.

        Returns:
            str: A string indicating path type.
        """
        if path.is_dir():
            return 'dir'
        elif path.is_file():
            return 'file'
        else:
            raise FileNotFoundError(f"File {path} not found")

    def _get_path_category(self, path: Path) -> str:
        """Determines path category.

        Determines path category for placing files locally.

        Args:
            path: Path str to determine category of.

        Returns:
            str: Category in which file belongs.
        """
        if str(path).startswith("/"):
            return "global"
        elif str(path).startswith("~"):
            return "local"

        return "custom"

    def _get_local_dest(self, path: Path) -> Path:
        """Gets local destination for copying.

        Gets local destination based on source path.

        Args:
            path: Path to build destination path from.

        Returns:
            str: Path pointing to local destination.
        """
        dest = ""

        if self.category == "global":
            dest = f"{self.local_base}/global/{path}"
        elif self.category == "local":
            relative = path.relative_to("~")
            dest = f"{self.local_base}/local/{relative}"
        else:
            relative = path.relative_to("~")
            dest = f"{self.local_base}/custom/{relative}"

        return Path(dest)

    def _get_local_src(self, path: Path) -> Path:
        """Gets local source path for copying.

        Gets local source path based on passed source path.

        Args:
            path: Path to build local source path from.

        Returns:
            str: Path pointing to local source.
        """
        src = ""

        if str(path).startswith("~"):
            path = Path(str(path).replace("~/", ""))

        if self.category == "global":
            src = f"{self.local_base}/global{path}"
        elif self.category == "local":
            src = f"{self.local_base}/local/{path}"
        else:
            src = f"{self.local_base}/custom/{path}"

        return Path(src)

   # ? Maybe rename these two methods to fetch/push
    def update(self) -> None:
        """Fetches dotfiles from given path"""
        destination = self._get_local_dest(self.absolute)

        try:
            path_type = self._get_path_type(self.absolute)
            handler = self.factory.get_handler(path_type)
            handler.update(self.absolute, destination)
        except Exception as e:
            print(f"[!] Skipping {self.path}: {e}")

    def bootstrap(self, backup: bool, overwrite: bool) -> None:
        """Bootstraps dotfiles to given path."""
        src = self._get_local_src(self.path)

        try:
            path_type = self._get_path_type(src)
            handler = self.factory.get_handler(path_type)
            handler.bootstrap(src, self.absolute, backup, overwrite)
        except Exception as e:
            print(f"[!] Skipping {self.path}: {e}")
