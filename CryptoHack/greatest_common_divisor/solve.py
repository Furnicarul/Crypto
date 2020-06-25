from pwn import *
#context.level = 'debug'

a = 66528
b = 52920

def cmmdc(a, b):
	if a%b == 0:
		return b
	return cmmdc(b, a%b)

log.info(cmmdc(a, b))
