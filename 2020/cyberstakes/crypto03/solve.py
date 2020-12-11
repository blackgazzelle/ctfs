import binascii
def decrypt(data, otp):
    out = []
    for i in range (0, len(data)):
        out.append(data[i] ^ otp[i % len(otp)])
    return bytes(out)

f = open("document.encrypted", "r")
flag = ""
for line in f:
    flag += line.strip()
flag = binascii.unhexlify(flag)
key = "The following encoded individuals are to be given a $27.3k bonus"
key = key.encode('utf-8')
otp = decrypt(flag[0:64], key)
flag = decrypt(flag, otp)
print(flag.decode('utf-8'))
