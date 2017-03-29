#!/usr/bin/env python3

import argparse
import json
import urllib.request

if __name__ == '__main__':

  parser = argparse.ArgumentParser ()
  parser.add_argument ('-v', '--verbose', help = 'Enable Verbose Mode', action = 'store_true')
  parser.add_argument ('-ip', help = 'IP Address to Test')
  args = parser.parse_args ()

  if args.ip:
    location_url = 'http://ipinfo.io/{:}/json'.format(args.ip)
  else:
    location_url = 'http://ipinfo.io/json'

  if args.verbose:
    print ('Retrieving location information ...')

  location_facts = json.loads ((urllib.request.urlopen (location_url).read ())
                                                       .decode ("utf-8"))

  print ('This IP is in {:}, {:}, {:}.'.format (location_facts ['city'],
                                                location_facts ['region'],
                                                location_facts ['country']))

  if args.verbose:
    print ('All done.')
