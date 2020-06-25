import operator
#context.level = 'debug'

string = "label"
xor_int = 13

flag = ""
for s in string:
        flag += chr(ord(s) ^ xor_int)

print("crypto{"+flag+"}")
