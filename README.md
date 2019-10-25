# Nomad

Dotfiles on the move

### Usage

1. Clone repository using `git clone https://github.com/tperich/nomad`.
2. Enter the directory and [install requirements](#install-requirements) using `pip3 install -r requirements.txt`.
3. Create a copy of [config.example.yml](./config.example.yml) called `config.yml` and place your dotfile paths inside.
4. Run `./nomad.py -u` to get the dotfiles from the system.
5. Run `./nomad.py -b` if you want to deploy dotfiles to the system.

Your dotfiles will be inside the dotfiles folder inside nomad directory.

### Other examples

Bootstrap dotfiles to system, create backups, and overwrite backups if they already exist.

`./nomad.py -b --backup --overwrite`

Deploy dotfiles using "ubuntu" profile.

`./nomad.py -u -p ubuntu`

Use a custom config.yml to update dotfiles from.

`./nomad.py -u -c ~/Desktop/dotfile-config.yml`

Print config and exit.
`./nomad.py --show`

### Roadmap

- [ ] Add file/dir filtering based on .gitignore files
- [ ] Group backups into a single user-defined directory
- [ ] Add support for achiving and/or compressing backup files
- [ ] Write tests & documentation
- [ ] Start versioning, package and distribute on PyPi

##### Install requirements

Note that we're using `pip3` here for python3. Depending on your system you might want to use just `pip`. You can check which version of python your pip uses by running `pip -V`.
