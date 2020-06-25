#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
from pwn import *
from binascii import *
import json

def solve(encoding, challenge_words):
	if encoding == "base64":
		encoded = base64.b64decode(challenge_words.encode()).decode() # wow so encode
	elif encoding == "hex":
		encoded = unhexlify(challenge_words.encode('utf-8')).decode("utf-8")
	elif encoding == "rot13":
		encoded = codecs.decode(challenge_words, 'rot_13')
	elif encoding == "bigint":
		encoded = unhexlify(challenge_words[2:].encode("utf-8")).decode('utf-8')
	elif encoding == "utf-8":
		encoded = ''.join([chr(b) for b in challenge_words])
	return encoded


p = connect("socket.cryptohack.org", 13377)

for _ in range(101):
	data = json.loads(p.recvline())
	print(data)
	sol = solve(data['type'], data['encoded'])
	sol = '{"decoded"' + ' : ' + '"' + sol + '"' + '}'
	print(sol)
	p.sendline(sol)


   