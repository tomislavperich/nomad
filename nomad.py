#!/usr/bin/env python3
#                                               ██
#                                              ░██
#  ███████   ██████  ██████████   ██████       ░██
# ░░██░░░██ ██░░░░██░░██░░██░░██ ░░░░░░██   ██████
#  ░██  ░██░██   ░██ ░██ ░██ ░██  ███████  ██░░░██
#  ░██  ░██░██   ░██ ░██ ░██ ░██ ██░░░░██ ░██  ░██
#  ███  ░██░░██████  ███ ░██ ░██░░████████░░██████
# ░░░   ░░  ░░░░░░  ░░░  ░░  ░░  ░░░░░░░░  ░░░░░░
"""Dotfiles on the move.

Update, bootstrap, delete, backup your dotfiles with minimum efffort.
Use profiles and define everything in a single file.
"""

import os
import argparse

import yaml

from handlers import Config
from helpers.file_helper import find_file


def parse_args() -> argparse.Namespace:
    """Parses command line arguments.

    Parses command line arguments and returns a dictionary.

    Returns:
        dict: A dict containing passed arguments and their values.
        For example:

        { 
            "config": "./config.yml"
        }
    """
    parser = argparse.ArgumentParser(
        prog="nomad",
        description="Dotfiles on the move",
    )
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        metavar='config_file',
        help="Path to config file",
    )

    dotfile_args = parser.add_mutually_exclusive_group()
    dotfile_args.add_argument(
        "-u", "--update",
        action="store_true",
        help="Update config files",
    )
    dotfile_args.add_argument(
        "-b", "--bootstrap",
        action="store_true",
        help="Bootstrap config files",
    )

    return parser.parse_args()


def find_config() -> str:
    """Attempts to find config.

    Looks for config.yml in usual directories.

    Returns:
        str: File path string if file is found, exists otherwise.
    """
    file_name = "config.yml"
    etc_dir = "/etc/nomad"
    curr_dir = os.getcwd()
    home_dir = os.getenv("HOME")
    config_dir = f"{home_dir}/.config"
    conf_env = os.getenv("NOMAD_CONF")

    dirs = [
        conf_env,
        curr_dir,
        home_dir,
        config_dir,
        etc_dir,
    ]

    try:
        return find_file(dirs, file_name)
    except FileNotFoundError as e:
        print("[!] No config found on the system")
        exit(1)


args = parse_args()
conf_path = args.config or find_config()
config = Config(conf_path)
