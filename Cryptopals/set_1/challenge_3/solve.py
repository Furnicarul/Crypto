from pwn import *
#context.level = 'debug'

encoded = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
decoded = encoded.decode("hex")
log.info(decoded)

string = "ETAOIN SHRDLU"

expected = "Cooking"

for i in range(256):
	flag = xor(decoded, i)
	if(expected in flag):
		print(flag)
		print(i)
		exit()

exit()
