#!/usr/bin/env python3

# ls.py
#
# Simple implementation of Unix "ls" command.
#   Prints list of files in the current directory. Does not include directories.
#
# Attempts to naively guess file contents based on file extension.
#   Requires "filetypes.json". If this file is not found, simply 
#   displays file names from the current directory.
#
# AMJ
# 2017-03-29

import json
import os

JSON_FILE = 'filetypes.json'

def json_file_found ():
    """
        Checks if required json file is present and can be read. Does not 
        check format.
    """

    try:
        jf = open (JSON_FILE, 'r')
        jf.close ()
        return True
    except IOError:
        return False

def load_filetype_dictionary ():
    """
        Loads contents of "filetypes.json" into a dictionary that will serve as a look-up table.
        Returns: Dictionary, keyed on file extension, of likely file types.
    """

    jf = open (JSON_FILE, 'r')
    js = json.loads (jf.read ())

    filetype_lookup = {}

    for entry in js:
        filetype_lookup [entry ['file_extension']] = entry ['contents']

    return filetype_lookup

def print_directory_name ():
    """
        Print name of current working directory, neatly formatted.
        Returns: Nada.
    """

    print ('Listing of "{:}":'.format (os.getcwd ()))

def print_file_names (filetype_lookup, print_types):
    """
        Print file names in the current working directory. If print_types is
        True, also attempt to guess content types.
        Returns: Nothing, zippo, nicks.
    """

    for file in sorted (os.listdir ()):
        if os.path.isfile (file) and print_types:
            if '.' not in file:
                file_type = 'Unknown - no file extension.'
            elif '.' + file.split ('.')[1] in filetype_lookup:
                file_type = filetype_lookup ['.' + file.split ('.')[1]]
            else:
                file_type = 'Unknown - not in list.'
            print ('{:32s} -- {:}'.format (file, file_type))

        elif os.path.isfile (file):
            print (file)
 
#
# Main Program
#

if __name__ == '__main__':

    print_directory_name ()

    if json_file_found ():
        filetype_lookup = load_filetype_dictionary ()
        print_file_names (filetype_lookup, True)
    else:
        print_file_names ({}, False)