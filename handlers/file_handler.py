from pathlib import Path


class FileHandler():
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
