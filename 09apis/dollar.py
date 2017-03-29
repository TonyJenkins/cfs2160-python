#!/usr/bin/env python3

import argparse
import json
import urllib.request

if __name__ == '__main__':

  parser = argparse.ArgumentParser ()
  parser.add_argument ('-v', '--verbose', help = 'Enable Verbose Mode', action = 'store_true')
  args = parser.parse_args ()

  base_currency = 'GBP'
  exchange_url = 'http://api.fixer.io/latest?base=' + base_currency

  if args.verbose:
    print ('Retrieving exchange information ...')

  exchange_facts = json.loads ((urllib.request.urlopen (exchange_url).read ()).decode ("utf-8"))

  print ('1 English Pound is currently worth {:} American Dollars.'.format (exchange_facts ['rates']['USD']))

  if args.verbose:
    print ('All done.')
