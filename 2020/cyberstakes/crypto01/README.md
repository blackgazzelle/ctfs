TF: Cyberstakes 2020
Challenge: Rotate Me

Category: crypto

Points: 20

Difficulty: Introductory

## Instructions

***Description***

Our security manager, Julius, is confident nobody can break his encryption and
so left the flag for everyone to see. [ciphered_flag.txt](ciphered_flag.txt)

***Hints***

Does knowing the flag format give you any information about how the flag was encrypted?
When in [Rome](https://en.wikipedia.org/wiki/Caesar_cipher)?
Julius is notorious for playing games with the problem names...

## Solution

This is simply a caesar cipher which we can easily figure out from the
challenge title as a roation cipher is almost always a caesar cipher.
We can also test this theory if we take the original flag:
IKQ{KzGxBw_NcV_nWz_ItT_dPGHoijR} and we try to get the known flag
format, so from I to A that would be 8. After that we can simply
write a tr command in bash to do the translation for us which gave
the flag. The command looks like this
`cat ciphered_flag.txt | tr 'I-ZA-Hi-za-h' 'A-Za-z'`
running that we get the flag ![solution](solution.png)

## Flag

`ACI{CrYpTo_FuN_fOr_AlL_vHYZgabJ}`

## Mitigation

The problem highlighted here is a weak cipher. A caesar cipher
is a weak and normally hackable. The best way to mitigate this
is to use a stronger encryption to encode the flag.
