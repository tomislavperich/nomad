import os
from typing import List


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


def read_gitignore(path: str) -> List[str]:
    """Returns rules from a gitignore file.

    Returns a list of rules from a "gitignore" file.
    Returns an empty list if file does not exist.

    Args:
        path: Path of a file containing ignore rules.

    Returns:
        list: Returns a list of ignore rules from file.
    """
    ignore_rules: List[str] = []

    if os.path.exists(path):
        with open(path, "r") as f:
            for rule in f.readlines():
                ignore_rules.append(rule.rstrip())

    return ignore_rules
