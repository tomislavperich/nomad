#!/usr/bin/sh
if ! command -v python3 > /dev/null; then
    sudo apt install python3 python3-pip -y
fi
./0_setup.py
