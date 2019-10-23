# Nomad

Dotfiles on the move

### Usage

1. Clone repository using `git clone https://github.com/tperich/nomad`.
2. Enter the directory and [install requirements](#install-requirements) using `pip3 install -r requirements.txt`.
3. Edit [config.yml](./config.yml) and place your dotfile paths.
4. Run `./nomad.py -u` to get the dotfiles from the system.
5. Run `./nomad.py -b` if you want to deploy dotfiles to the system.

Your dotfiles will be inside the dotfiles folder inside nomad directory.

### Other examples

Bootstrap dotfiles to system, create backups, and overwrite backups if they already exist.

`./nomad.py -b --backup --overwrite`

Use profile "ubuntu" to deploy dotfiles and show config.

`./nomad.py -u -p ubuntu --show`

Use a custom config.yml to update dotfiles from.

`./nomad.py -u -c ~/Desktop/dotfile-config.yml`

### Roadmap

- [ ] Add file/dir filtering based on .gitignore files
- [ ] Group backups into a single user-defined directory
- [ ] Add support for achiving and/or compressing backup files
- [ ] Write tests & documentation
- [ ] Start versioning, package and distribute on PyPi

##### Install requirements

Note that we're using `pip3` here for python3. Depending on your system you might want to use just `pip`. You can check which version of python your pip uses by running `pip -V`.
