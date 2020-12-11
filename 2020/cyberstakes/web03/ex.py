#!/usr/bin/env python3
import requests
url = 'http://challenge.acictf.com:2342/flag_checker.js'
r = requests.get(url)
print(r.text)
