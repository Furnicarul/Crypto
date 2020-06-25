from pwn import *
#context.level = 'debug'

encoded1 = "1c0111001f010100061a024b53535009181c"
decoded1 = encoded1.decode("hex")

encoded2 = "686974207468652062756c6c277320657965"
decoded2 = encoded2.decode("hex")

xored = xor(decoded1, decoded2)
print(xored)
