#!/usr/bin/env python3

# rm.py
#
# Simple implementation of Unix "rm" command.
#
# AMJ
# 2013-12-09

import argparse
import os

#
# Main Program
#

if __name__ == '__main__':

  parser = argparse.ArgumentParser ()
  parser.add_argument ('-v', '--verbose', help = 'Enable Verbose Mode', action = 'store_true')
  parser.add_argument ('-c', '--careful', help = 'Enable Careful Mode', action = 'store_true')
  parser.add_argument ('file_name', help = 'Original Name')

  args = parser.parse_args ()

  if not os.path.exists (args.file_name):
    print ('{:}: no such file'.format (args.file_name))
  elif os.path.exists (args.file_name):
    
    if args.verbose:
      print ('Removing "{:}".'.format (args.file_name))

    carefully_now = ''
    if args.careful:
      carefully_now = input ('Are you sure? (y/n): ')
      
    if carefully_now in ['y', 'Y', 'yes', 'Yes', 'Yup', 'Indeed', 'Sure'] or not args.careful:
      os.remove (args.file_name)
  
  else:
    print ('Cannot access source: "{:}".'.format (args.file_name))