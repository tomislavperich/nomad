import os
import shutil
from pathlib import Path


class FileHandler():
    """Handles file operations. """

    def update(self, src: Path, dst: Path) -> None:
        """Copies a file.

        Copies file from system.

        Args:
            src: Absolute Path to file source.
            dest: Absolute Path to file destination.
        """
        print(f"[+] Updating [file]: \t{str(dst).ljust(30)} <- {src}")
        if not dst.parent.exists():
            dst.parent.mkdir(parents=True)

        try:
            shutil.copy(src, dst)
        except shutil.Error as e:
            print(f"[!] Error: {e}")

    def bootstrap(
        self,
        src: Path,
        dst: Path,
        backup: bool = False,
        overwrite: bool = False
    ) -> None:
        """Bootstraps a file.

        Bootstraps file to system.

        Args:
            src: Absolute Path to file source.
            dst: Absolute Path to file destination.
            backup: Boolean indicating whether file should be backed up.
            overwrite: Boolean indicating whether to overwrite backups.
        """
        print(f"[+] Strapping [file]: \t{str(src).ljust(30)} -> {dst}")

        if not dst.parent.exists():
            dst.parent.mkdir()

        if dst.exists():
            if backup:
                self.backup(dst, overwrite)

            self.delete(dst)

        try:
            shutil.copy(src, dst)
        except shutil.Error as e:
            print(f"[!] Error {e}")

    def backup(self, path: Path, overwrite: bool = False) -> None:
        """Creates a backup of file.

        Creates a backup of [file] named [file].backup

        Args:
            path: Path to file to back up.
        """
        backup_path = Path(f"{path}.backup")

        if backup_path.exists() and not overwrite:
            try:
                choice = input("Backup already exists. Overwrite? [Y/n]: ")
            except KeyboardInterrupt:
                exit(0)

            if choice == ("y" or "Y" or ""):
                self.delete(backup_path)
        else:
            self.delete(backup_path)

        try:
            shutil.copy(path, f"{path}.backup")
        except shutil.Error as e:
            print(f"[!] Error: {e}")

    def delete(self, path: Path) -> None:
        """Deletes a file.

        Args:
            path: Path to file to delete.
        """
        if path.exists():
            os.remove(path)
