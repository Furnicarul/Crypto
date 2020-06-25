from pwn import *
from Crypto.Util import *
from Crypto.Util.number import long_to_bytes
import base64
import json

#context.level = 'debug'

HOST = "socket.cryptohack.org"
PORT = 13377

FLAG = ""
ENCODINGS = [
    "base64",
    "hex",
    "rot13",
    "bigint",
    "utf-8",
]

p = remote(HOST, PORT)
print(p.recv())

def encodings(self):
	if ENCODINGS[0] == "base64":
		encoded = base64.b64decode()
	elif ENCODINGS[1] == "hex":
		encoded = self.decode("hex")
	elif ENCODINGS[2] == "rot13":
		encoded = self.decode("rot13")
	elif ENCODINGS[3] == "bigint":
		encoded = long_to_bytes()
	elif ENCODINGS[4] == "utf-8":
		encoded = [ord(b) for b in self]

