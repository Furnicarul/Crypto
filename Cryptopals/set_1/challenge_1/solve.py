import base64
from pwn import * 
#context.level = 'debug'

encoded = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
decoded = encoded.decode("hex")
log.info(decoded)
