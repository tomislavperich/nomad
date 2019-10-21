import shutil
from pathlib import Path


class FileHandler():
    def update(self, src: Path, dst: Path) -> None:
        """Copies a file.

        Copies file from source to destination.

        Args:
            src: Absolute Path to file to copy from.
            dest: Absolute Path to file to copy to.
        """
        # Does parent directory exist?
        print(f"[+] Updating [file]: \t{str(src).ljust(30)} -> {dst}")
        if not dst.parent.exists():
            dst.parent.mkdir(parents=True)

        try:
            shutil.copy(src, dst)
        except shutil.Error as e:
            print(f"[!] Error: {e}")

    def bootstrap(self, src: Path, dst: Path) -> None:
        """
        home_path = os.getenv("HOME")
        remote_path = f"{home_path}/{path}"

        if not remote_path.exists():
            remote_path.mkdir()

        shutil.copyfile(path, remote_path)
        """
        print("Bootstrapping file, hurr durr...")
