#!/usr/bin/env python
import os
from os.path import expanduser
import shutil
import socket

# a dict of all the files I care about
DOTFILES = {
    "BASH_RC": '.bash_rc',
    "BASH_PROFILE": ".bash_profile",
    "VIM": ".vimrc",
    "S3CFG": ".s3cfg",
    "SHEETS": ".sheetsCredentials.json",
    "AWS_CREDENTIALS": ".aws/credentials",
}

# define home
HOME = expanduser("~")
# destination folder is name of computer
DESTINATION = socket.gethostname()

if not os.path.exists(DESTINATION):
    os.mkdir(DESTINATION)

# loop over dotfiles dict, copying original over to repo
for key, value in DOTFILES.items():
    # build the path from the filename
    try:
        filepath = os.path.join(HOME, value)
        destpath = os.path.join(DESTINATION, key)
        # copy and give new name from DOTFILES key
        shutil.copy(filepath, destpath)
        print("Copied {}".format(key))
    except:
        print("Couldn't copy {}".format(key))
        pass
