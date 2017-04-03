#!/usr/bin/env python3

# mv.py
#
# Simple implementation of Unix "mv" command.
#
# AMJ
# 2017-03-29

import argparse
import os
import shutil

#
# Main Program
#

if __name__ == '__main__':

    parser = argparse.ArgumentParser ()
    parser.add_argument ('-v', '--verbose', help = 'Enable Verbose Mode', action = 'store_true')
    parser.add_argument ('-c', '--careful', help = 'Enable Careful Mode', action = 'store_true')
    parser.add_argument ('source_file', help = 'Original Name')
    parser.add_argument ('destination_file', help = 'New Name')
    args = parser.parse_args ()

    if args.careful and os.path.exists (args.destination_file):
        print ('Destination File "{:}" exists. Will not copy.'.format (args.destination_file))
    elif os.path.exists (args.source_file):
        if args.verbose:
            print ('Renaming "{:}" to "{:}".'.format (args.source_file, args.destination_file))
        shutil.move (args.source_file, args.destination_file)
    else:
        print ('Cannot access source: "{:}".'.format (args.source_file))
