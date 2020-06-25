from pwn import *
from binascii import *
from base64 import *
from Crypto.Cipher import *

def dec_ecb(enc, key):
	cipher = AES.new(key, AES.MODE_ECB)
	plaintext = cipher.decrypt(enc)
	return plaintext

def main():
	key = "YELLOW SUBMARINE"
	with open("data.txt") as data_file:
		enc = base64.b64decode(data_file.read())
	message = dec_ecb(enc, key)
	log.info(message)

if __name__ == "__main__":
	main()
