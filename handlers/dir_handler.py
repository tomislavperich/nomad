from pathlib import Path


class DirHandler():
    def update(self, path: Path) -> None:
        """
        home_path = os.getenv("HOME")
        local_path = path.relative_to(home_path)

        if not local_path.exists()
            path.mkdir()

        shutil.copy(path, local_path)
        """
        print("Updating dir, hurr durr...")

    def bootstrap(self, path: Path) -> None:
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
