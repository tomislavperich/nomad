import shutil
from pathlib import Path


class DirHandler():
    """Handles directory operations."""

    def update(self, src: Path, dst: Path, overwrite: bool = False) -> None:
        """Copies a directory.

        Copies directory from system.

        Args:
            src: Absolute Path to directory source.
            dest: Absolute Path to directory destination.
        """
        print(f"[+] Updating [dir]: \t{str(dst).ljust(30)} <- {src}")
        if dst.exists():
            shutil.rmtree(dst)

        try:
            shutil.copytree(src, dst)
        except shutil.Error as e:
            print(f"[!] Error: {e}")

    def bootstrap(
        self,
        src: Path,
        dst: Path,
        backup: bool = False,
        overwrite: bool = False,
    ) -> None:
        """Bootstraps a directory.

        Bootstraps directory to system.

        Args:
            src: Absolute Path to directory source.
            dst: Absolute Path to directory destination.
            backup: Boolean indicating whether files should be backed up.
            overwrite: Boolean indicating whether to overwrite backups.
        """
        print(f"[+] Strapping [dir]: \t{str(src).ljust(30)} -> {dst}")
        if dst.exists():
            if backup:
                self.backup(dst, overwrite)

            self.delete(dst)

        try:
            shutil.copytree(src, dst)
        except shutil.Error as e:
            print(f"[!] Error: {e}")

    def backup(self, path: Path, overwrite: bool = False) -> None:
        """Creates a backup of dir.

        Creates a backup of [dir] named [dir].backup.

        Args:
            path: Path to dir to back up.
        """
        backup_path = Path(f"{path}.backup")

        if backup_path.exists() and not overwrite:
            try:
                choice = input("Backup exists. Overwrite? [Y/n]: ")
            except KeyboardInterrupt:
                exit(0)

            if choice == ("y" or "Y" or ""):
                self.delete(backup_path)
        else:
            self.delete(backup_path)

        try:
            shutil.copytree(path, f"{path}.backup")
        except shutil.Error as e:
            print(f"[!] Error: {e}")

    def delete(self, path: Path) -> None:
        """Deletes a dir.

        Args:
            path: Path to directory to delete.
        """
        if path.exists():
            shutil.rmtree(path)
