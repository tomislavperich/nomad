import argparse


class Parser():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="nomad",
            description="Dotfiles on the move",
        )

        self._add_args()

    def _add_args(self):
        """Parses command line arguments.

        Parses command line arguments and returns them.

        Returns:
            dict: A dict containing parsed arguments and their values.
            For example:

            { 
                "config": "./config.yml"
            }
        """
        self.parser.add_argument(
            "-c",
            "--config",
            type=str,
            metavar='config_file',
            help="Path to config file",
        )
        self.parser.add_argument(
            "-p", "--profile",
            type=str,
            metavar="profile",
            help="Profile to use"
        )
        self.parser.add_argument(
            "--show",
            dest="show",
            action="store_true",
            help="Show config file"
        )
        self.parser.add_argument(
            "--backup",
            action="store_true",
            help="Back up existing files on bootstrap",
        )
        self.parser.add_argument(
            "--overwrite",
            action="store_true",
            help="Overwrite existing backups",
        )

        self.dotfile_args = self.parser.add_mutually_exclusive_group()
        self.dotfile_args.add_argument(
            "-u", "--update",
            action="store_true",
            help="Update dotfiles",
        )
        self.dotfile_args.add_argument(
            "-b", "--bootstrap",
            action="store_true",
            help="Bootstrap dotfiles",
        )

    def get_args(self):
        return self.parser.parse_args()
