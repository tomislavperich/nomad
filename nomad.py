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

from handlers import Config, Dotfile
from helpers.file_helper import find_file


def parse_args() -> dict:
    """Parses command line arguments.

    Parses command line arguments and returns them.

    Returns:
        dict: A dict containing parsed arguments and their values.
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
    parser.add_argument(
        "-p", "--profile",
        type=str,
        metavar="profile",
        help="Profile to operate on"
    )
    parser.add_argument(
        "--show",
        dest="show",
        action="store_true",
        help="Show config file"
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

    args = parser.parse_args()
    return vars(args)


def find_config() -> str:
    """Attempts to find config file.

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


def update_dotfiles(dotfiles: list):
    """Updates dotfiles from list."""
    for dotfile in dotfiles:
        dotfile.update()


def bootstrap_dotfiles(dotfiles: list):
    """Bootstraps dotfiles from list."""
    for dotfile in dotfiles:
        dotfile.bootstrap()


def main():
    args = parse_args()
    conf_path = args["config"] or find_config()
    profile = args["profile"]

    config = Config(conf_path, profile)
    paths = config.paths

    dotfiles = []
    for path in paths:
        dotfiles.append(Dotfile(path))

    if args["show"]:
        config.print_config()

    if args["update"]:
        update_dotfiles(dotfiles)
    elif args["bootstrap"]:
        bootstrap_dotfiles(dotfiles)


if __name__ == '__main__':
    main()
