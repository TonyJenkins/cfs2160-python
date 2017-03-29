#!/usr/bin/env python3

import argparse
import json
import urllib.request

from secrets import weather_api

if __name__ == '__main__':

  parser = argparse.ArgumentParser ()
  parser.add_argument ('-v', '--verbose', help = 'Enable Verbose Mode', action = 'store_true')
  parser.add_argument ('-ip', help = 'IP Address for Weather')
  args = parser.parse_args ()

  if args.ip:
    location_url = 'http://ipinfo.io/{:}/json'.format(args.ip)
  else:
    location_url = 'http://ipinfo.io/json'

  if args.verbose:
    print ('Retrieving location information ...')

  location_facts = json.loads ((urllib.request.urlopen (location_url).read ()).decode ("utf-8"))

  if args.verbose:
    print ('Building Weather Query ...')

  weather_url = 'http://api.wunderground.com/api/{:}/conditions/q/{:}.json'.format (weather_api, location_facts['loc'])

  if args.verbose:
    print ('Sending Weather Query ...')

  weather_facts = json.loads((urllib.request.urlopen(weather_url).read()).decode("utf-8"))

  print('This IP is in {:}, {:}, {:}. Where the weather is {:}.'.format(location_facts['city'], location_facts['region'],
                                                                        location_facts['country'],
                                                                        weather_facts['current_observation']['weather']))

  if args.verbose:
    print ('All done.')
