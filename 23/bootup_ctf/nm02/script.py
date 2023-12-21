from pwn import *
import struct

p = remote('3-nm03.bootupctf.net',8232)


print(p.recvuntil("\n"))

buf = p.recvuntil("\n")

print("buf is:",buf)

print(p.recvuntil("\n"))

decode = list(map(lambda x: int(x),buf.split(b'-')[:-1]))
with open('test', 'wb') as f:
    for i in decode:
        print(struct.pack('>h', i))
        f.write(struct.pack('>h', i))
