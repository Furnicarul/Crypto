from binascii import *
from pwn import *
import string
#context.level = 'debug'

with open('data.txt') as data_file:
    cipher_list = [
        unhexlify(line.strip())
        for line in data_file
    ]

def isprintable(s, codec='utf8'):
    try: s.decode(codec)
    except UnicodeDecodeError: return False
    else: return True

for x in range(256):
    for cipher in cipher_list:
        flag = xor(cipher, x)
	if isprintable(flag):
		print(flag)
