#!/usr/bin/env python3
import requests
import binascii

def send_attack(pt):
    url = 'http://challenge.acictf.com:62963'
    r = requests.post(f'{url}/register', data=dict(username=pt, password="asdf"))
    cookies = r.headers['Set-Cookie']
    ct = cookies[len('auth_token='):].split(';')[0]
    ct = binascii.unhexlify(ct)
    return ct

blockSize = 16
prefix = b'A' * blockSize * 2
secret_len = 18
chars = [bytes([i]) for i in range (32, 128)]

index = 0
secret = b''
for i in range(18):
    print(i)
    secretIndex = index // blockSize
    paddingOffset = (
        blockSize - (index % blockSize) - 1
    )
    pt = prefix + b'B' * paddingOffset

    secretCT = send_attack(pt)
    idx = secretIndex + 2
    for c in chars:
        posCT = send_attack(pt + secret + c)
        if (secretCT[(idx) * blockSize:(idx + 1) * blockSize] == posCT[(idx) * blockSize:idx + 1 * blockSize]):
            secret += c
            break
    index += 1

print(secret)
