import os
import shutil
from pathlib import Path


class DirHandler():
    def update(self, src: Path, dst: Path) -> None:
        """Copies a directory.

        Copies directory from source to destination.

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

    def bootstrap(self, src: Path, dest: Path) -> None:
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
