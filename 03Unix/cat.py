#!/usr/bin/env python3

# cat.py
#
# Simple implementation of Unix "cat" command.
#
# Allows more than one file on command line. Checks all files before generating
#   output (note race condition here). Incorporates "tac" command with "-r" flag.
#
# AMJ
# 2017-03-28

import argparse

def file_exists (filename):
    """
       Determine if a file with the given name exists in the current directory and can be opened for reading.
       Returns: True iff it exists and can be opened, False otherwise.
       :param filename: Filename to check.
       :return True if file exists.
    """

    try:
        f = open (filename, 'r')
        f.close ()

        return True

    except IOError:
        return False

def missing_files (file_list):
    """
        Checks if all the files named in the list exist and can be opened.
        Returns: List of the files that cannot be opened, so empty list if  all is well.
        :param file_list: List of file names to be checked.
        :return List of missing files.
    """

    naughty_files = []

    for file in file_list:
        if not file_exists (file):
            naughty_files.append (file)
  
    return naughty_files

def write_file (file_name):
    """
       Display the contents of the file named on standard output. File is assumed to exist and be readable.
       Returns: Nowt.
       :param file_name: File name to be written.
    """

    f = open (file_name, 'r')
    print (f.read ())
    f.close ()

def write_file_reversed (file_name):
    """
      Display the contents of the file name on standard output, in reverse order. File is assumed to exist and 
      be readable.
      Returns: Nothing.
    """

    f = open (file_name, 'r')
    contents = f.readlines ()
    contents.reverse ()

    for line in contents:
      print (line)
  
    f.close ()

def print_files (file_list, verbose, reverse):
    """Print out the contents of all the files named in file_list. If verbose is
     True, format output a little with a header block and some separators. If
     reverse is True, contents are reversed line-by-line. 
     Otherwise, just output files as they are.
     Returns: A sense of a job well done.
    """

    for file_name in file_list:
        if verbose:
            print ('')
            print ('**' + (len (file_name) * '*') + '**')
            print ('* ' + file_name + ' *')
            print ('**' + (len (file_name) * '*') + '**')
            print ('')

        if not reverse:
            write_file (file_name)
        else:
            write_file_reversed (file_name)

        if verbose:
            print ('')
            print (80 * '-')
            print ('')

#
# Main Program
#

if __name__ == '__main__':

    parser = argparse.ArgumentParser ()
    parser.add_argument ('-v', '--verbose', help = 'Enable Verbose Mode', action = 'store_true')
    parser.add_argument ('-r', '--reverse', help = 'Reverse File Contents', action = 'store_true')
    parser.add_argument ('file_list', nargs = '+', help = 'List of Files to Display')
    args = parser.parse_args ()

    missing = missing_files (args.file_list)

    if missing == []:
        print_files (args.file_list, args.verbose, args.reverse)
    else:
        for file in missing:
            print ("{:}: file not found.".format (file))