from pwn import *
#context.level = 'debug'

xor_byte = 1

encoded = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
decoded = encoded.decode("hex")

for i in range(256):
	flag = xor(decoded, i)
	if("crypto" in flag):
		log.info(i)
		log.info(flag)
		exit()
