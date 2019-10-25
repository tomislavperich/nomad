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

import yaml

from handlers import Config, Dotfile
from helpers.argparse_helper import Parser
from helpers.config_helper import find_config


class Main:
    def __init__(self, config: Config):
        self.config = config
        self.dotfiles = self._init_dotfiles(config)

    def _init_dotfiles(self, config):
        dotfiles = []

        for path in config.paths:
            dotfiles.append(Dotfile(path))

        return dotfiles

    def update(self):
        if self.config.profile:
            print(f"Using profile: {self.config.profile}")

        for dotfile in self.dotfiles:
            dotfile.update()

    def bootstrap(self, backup, overwrite):
        if self.config.profile:
            print(f"Using profile: {self.config.profile}")

        for dotfile in self.dotfiles:
            dotfile.bootstrap(backup, overwrite)


if __name__ == "__main__":
    parser = Parser()
    args = parser.get_args()

    config_path = args.config or find_config()
    profile_name = args.profile

    config = Config(config_path, profile_name)
    nomad = Main(config)

    if args.show:
        config.print_config()
        exit(0)

    if args.update:
        nomad.update()
    elif args.bootstrap:
        nomad.bootstrap(args.backup, args.overwrite)
