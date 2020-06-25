from pwn import *
from binascii import *
#context.level = 'debug'

key= "ICE"
enc = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"

for i in enc:
	key= "ICE"
	enc = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"

	count = 0
	flag = xor(i, key[count])

	count += 1
	if count == len(key):
		count = 0

	print(hexlify(bytearray(flag)))
