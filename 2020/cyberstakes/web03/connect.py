#!/usr/bin/env python3
import requests
url = 'http://challenge.acictf.com:2342/'
r = requests.get(url)
print(r.text)
print(r.cookies['most_out_of_site_flag'])
url = 'http://challenge.acictf.com:2342/flag_checker.js'
r = requests.get(url)
print(r.text)
