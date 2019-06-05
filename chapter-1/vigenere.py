import string

def encrypt_vigenere(pt, key):
	alphabet = string.ascii_lowercase
	cnt = 0
	ct = ""
	for letter in pt:
		if letter in alphabet:
			ct += alphabet[(alphabet.find(letter) + alphabet.find(key[cnt])) % len(alphabet)]
			cnt = (cnt + 1) % len(key)
		else:
			ct += letter
	return ct


def decrypt_vigenere(ct, key):
	alphabet = string.ascii_lowercase
	cnt = 0
	pt = ""
	for letter in ct:
		if letter in alphabet:
			pt += alphabet[(alphabet.find(letter) - alphabet.find(key[cnt])) % len(alphabet)]
			cnt = (cnt + 1) % len(key)
		else:
			pt += letter
	return pt


def test():
	print(encrypt_vigenere("hello world!", "key")) # rijvs uyvjn!
	print(decrypt_vigenere("rijvs uyvjn!", "key")) # hello world!


if __name__ == "__main__":
	test()
