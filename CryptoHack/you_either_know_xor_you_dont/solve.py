from pwn import *
#context.level = 'debug'

encoded = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
decoded = encoded.decode("hex")
log.info(decoded)

flag = ""
for i in encoded:
	for x in range(256):
		flag += chr(ord(i) ^ x)
		print(flag)
	exit()
