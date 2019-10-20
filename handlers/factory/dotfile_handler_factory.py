from ..file_handler import FileHandler
from ..dir_handler import DirHandler


class DotfileHandlerFactory:
    def get_handler(self, path_type: str):
        """Gets dotfile handler based on path type

        Args:
            path_type: Type of path whether it was dir or file

        Returns:
            DotfileHandler: Handler for dotfiles
        """
        if path_type == 'file':
            return FileHandler()
        elif path_type == 'dir':
            return DirHandler()
        else:
            raise ValueError(f"Unknown path type: {path_type}")
