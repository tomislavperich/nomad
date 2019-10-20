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


def parse_args() -> argparse.Namespace:
    """Parses command line arguments.

    Parses command line arguments and returns a dictionary.

    Returns:
        A dict containing passed arguments and their values.
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
        nargs='?',
        default=os.getcwd(),
        metavar='config_file',
        help="Path to config file",
    )

    return parser.parse_args()


args = parse_args()
config = Config(args.config)
config.print()
