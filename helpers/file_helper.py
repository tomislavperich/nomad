import os


def find_file(dirs: list, file_name: str) -> str:
    """Looks for file in given directories.

    Iterates over list of directories and checks if 
    file_name is present.

    Args:
        dirs: List of directories to look in.
        file_name: Name of the file to look for.

    Returns:
        str: Full path to the file.

    Raises:
        FileNotFoundError: If file is not found.
    """
    for location in dirs:
        full_path = f"{location}/{file_name}"
        if os.path.isfile(full_path):
            return full_path

    raise FileNotFoundError(f"File {file_name} not found")
