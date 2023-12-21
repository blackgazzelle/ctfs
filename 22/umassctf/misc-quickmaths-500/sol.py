from pwn import *

r = remote("34.148.103.218", "1228")
print(r.recvuntil("luck!").decode())
print(r.recvline().decode())
for i in range(1000):
    print(i)
    print(r.recvline().decode())
    math = r.recvline()
    print(math.decode())
    print(eval(math.decode()))
    r.sendline(str(eval(math)))
print(r.recv())
r.close()
