from pwn import *
from Crypto.Util.Padding import pad, unpad

block_size = 20
data = "YELLOW SUBMARINE"

log.info(_pad(data, block_size))
