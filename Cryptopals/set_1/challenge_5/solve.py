from pwn import *
from binascii import *
#context.level = 'debug'

def repeating_xor(key, enc):
	count = 0
	arr = []
	for i in enc:
		arr.append(ord(i) ^ ord(key[count]))

		count += 1
		if count == len(key):
			count = 0

	return hexlify(bytearray(arr))

key = "ICE"
enc = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"

encrypted = repeating_xor(key, enc)
log.info(encrypted)

