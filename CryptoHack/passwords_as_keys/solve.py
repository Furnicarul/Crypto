from Crypto.Cipher import AES
import hashlib
import random

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}

def main():
	key = hashlib.md5(keyword.encode()).digest()
	with open("words.txt") as data_file:
		words = [w.strip() for w in data_file]
	ciphertext = ""
	for ele in words:
		ciphertext += ele
	log.info(ciphertext)

if __name__ == "__main__":
	main()
