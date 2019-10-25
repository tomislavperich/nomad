import os

from .file_helper import find_file


def find_config(file_names: list = []) -> str:
    """Attempts to find config file.

    Looks for config.yml in usual directories.

    Args:
        file_names: Config file names to look for.

    Returns:
        str: File path string if file is found, exists otherwise.
    """
    if not file_names:
        file_names = ["config.yml", "config.example.yml"]

    etc_dir = "/etc/nomad"
    curr_dir = os.getcwd()
    home_dir = os.getenv("HOME")
    conf_env = os.getenv("NOMAD_CONF")
    config_dir = f"{home_dir}/.config/nomad"

    dirs = [
        conf_env,
        curr_dir,
        home_dir,
        config_dir,
        etc_dir,
    ]

    config = ""

    for file_name in file_names:
        try:
            config = find_file(dirs, file_name)
            break
        except:
            pass

    if not config:
        print("[!] No config found on the system")
        exit(1)

    return config
