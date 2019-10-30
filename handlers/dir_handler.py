import os
import shutil
from typing import List
from pathlib import Path

from helpers.file_helper import read_gitignore


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

        rules: List[str] = []

        if ".gitignore" in os.listdir(src):
            rules = read_gitignore(f"{src}/.gitignore")

        self.copy(src, dst, rules)

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

        if backup_path.exists():
            if overwrite:
                self.delete(backup_path)
            else:
                try:
                    choice = input("Backup exists. Overwrite? [Y/n]: ")
                except KeyboardInterrupt:
                    exit(0)

                if choice == ("y" or "Y" or ""):
                    self.delete(backup_path)
                else:
                    return

        self.copy(path, backup_path)

    def copy(self, src: Path, dst: Path, ignore_rules: List[str] = []) -> None:
        """Copies a dir.

        Args:
            src: Source path.
            dst: Destination path.
            rules: A list of ignore rules/patterns.
        """
        try:
            shutil.copytree(
                src, dst,
                ignore=shutil.ignore_patterns(*ignore_rules)
            )
        except shutil.Error as e:
            print(f"[!] Error: {e}")

    def delete(self, path: Path) -> None:
        """Deletes a dir.

        Args:
            path: Path to directory to delete.
        """
        if path.exists():
            shutil.rmtree(path)
