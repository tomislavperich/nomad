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
        help="Profile to use"
    )
    parser.add_argument(
        "--show",
        dest="show",
        action="store_true",
        help="Show config file"
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Back up existing files on bootstrap",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing backups",
    )

    dotfile_args = parser.add_mutually_exclusive_group()
    dotfile_args.add_argument(
        "-u", "--update",
        action="store_true",
        help="Update dotfiles",
    )
    dotfile_args.add_argument(
        "-b", "--bootstrap",
        action="store_true",
        help="Bootstrap dotfiles",
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


def update_dotfiles(dotfiles: list) -> None:
    """Updates dotfiles from list."""
    for dotfile in dotfiles:
        try:
            dotfile.update()
        except Exception as e:
            print(f"[!] Skipping {dotfile.path}, {e}")

    print("[+] Done!")


def bootstrap_dotfiles(
    dotfiles: list,
    backup: bool,
    overwrite: bool,
) -> None:
    """Bootstraps dotfiles from list."""
    for dotfile in dotfiles:
        try:
            dotfile.bootstrap(backup, overwrite)
        except Exception as e:
            print(f"[!] Skipping {dotfile.path}, {e}")

    print("[+] Done!")


def main():
    args = parse_args()
    conf_path = args["config"] or find_config()
    profile = args["profile"]

    config = Config(conf_path, profile)

    dotfiles = []
    for path in config.paths:
        dotfiles.append(Dotfile(path))

    if args["show"]:
        config.print_config()

    if args["update"]:
        update_dotfiles(dotfiles)
    elif args["bootstrap"]:
        bootstrap_dotfiles(
            dotfiles,
            args["backup"],
            args["overwrite"],
        )


if __name__ == '__main__':
    main()
