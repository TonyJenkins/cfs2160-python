#!/usr/bin/env python3

# find.py
#
# Simple implementation of Unix "find" command.
#
# List all the directories that contain a file with the given name.
#   Searches below the current folder by default, or below the home
#   folder if --home flag supplied.
#
# AMJ
# 2017-03-29

import argparse
from os import walk, getcwd
from os.path import expanduser

if __name__ == '__main__':

    parser = argparse.ArgumentParser ()
    parser.add_argument ('-v', '--verbose', help = 'Enable Verbose Mode', action = 'store_true')
    parser.add_argument ('--home', help = 'Search relative to $HOME', action = 'store_true')
    parser.add_argument ('file_to_find', help = 'Name of File to Find')
    args = parser.parse_args ()

    if not args.home:
        start_point = getcwd ()
    else:
        start_point = expanduser ('~')

    for root, dirs, files in walk (start_point):
        if args.file_to_find in files:
            print (root)