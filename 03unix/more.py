#!/usr/bin/env python3

# more.py
#
# Simple implementation of Unix "more" command.
#
# Allows more than one file on command line. Checks all files before generating
#   output (note race condition here).
#
# AMJ
# 2017-03-29

import argparse
from shutil import get_terminal_size


def file_exists (filename):
    """Determine if a file with the given name exists in the current directory
       and can be opened for reading.
       Returns: True iff it exists and can be opened, False otherwise.
    """

    try:
        f = open (filename, 'r')
        f.close ()

        return True

    except IOError:
        return False


def missing_files (file_list):
    """Checks if all the files named in the list exist and can be opened.
       Returns: List of the files that cannot be opened, so empty list if
                all is well.
    """

    naughty_files = []

    for file in file_list:
        if not file_exists (file):
            naughty_files.append (file)

    return naughty_files


def chomp (s):
    """Remove the last character from 's' and return the shortened string.
       Intended to remove end-of-line characters, but could also have a host
       of amusing uses.
       Returns: s, minus its last character, or an empty string if s was null.
    """

    return s [:-1]


def pager (text_to_display):
    """Display the text provided a screen at a time in the current terminal.
       Wait for any <CR> ended input before displaying next.
    """

    lines_per_chunk = get_terminal_size ().lines - 2
    number_of_chunks = len (text_to_display) // lines_per_chunk + 1

    for chunk in range (number_of_chunks):
        for line in text_to_display [chunk * lines_per_chunk: chunk * lines_per_chunk + lines_per_chunk]:
            print (chomp (line))
        input ('Press Return for More {0:.0%}  '.format (chunk / number_of_chunks))


def print_files (file_list, verbose):
    """Print out the contents of all the files named in file_list. If verbose is
       True, format output a little with a header block and some separators.
       Otherwise, just output files as they are.
       Returns: A sense of a job well done.
    """

    for file_name in file_list:
        output = []
        if verbose:
            output.append ('\n\n')
            output.append ('**' + (len (file_name) * '*') + '**' + '\n')
            output.append ('* ' + file_name + ' *' + '\n')
            output.append ('**' + (len (file_name) * '*') + '**' + '\n')
            output.append ('\n\n')

        f = open (file_name, 'r')
        for line in f.readlines ():
            output.append (line)
        f.close ()

        if verbose:
            output.append ('\n\n')
            output.append (80 * '-' + '\n')
            output.append ('\n\n')

        pager (output)


#
# Main Program
#

if __name__ == '__main__':

    parser = argparse.ArgumentParser ()
    parser.add_argument ('-v', '--verbose', help = 'Enable Verbose Mode', action = 'store_true')
    parser.add_argument ('file_list', nargs = '+', help = 'List of Files to Display')
    args = parser.parse_args ()

    missing = missing_files (args.file_list)

    if missing == []:
        print_files (args.file_list, args.verbose)
    else:
        for file in missing:
            print ('{:}: file not found.'.format (file))
