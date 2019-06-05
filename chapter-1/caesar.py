import string

def encrypt_caesar(pt, shift=13):
	alphabet = string.ascii_lowercase
	ct = ""
	for letter in pt:
		if letter in alphabet: # Ignore spaces, commas, etc.
			ct += alphabet[(alphabet.find(letter) + shift) % len(alphabet)]
		else:
			ct += letter
	return ct


def decrypt_caesar(ct, shift=13):
	alphabet = string.ascii_lowercase
	pt = ""
	for letter in ct:
		if letter in alphabet:
			pt += alphabet[(alphabet.find(letter) - shift) % len(alphabet)]
		else:
			pt += letter
	return pt


def test():
	print(encrypt_caesar("hello world!")) # uryyb jbeyq!
	print(decrypt_caesar("uryyb jbeyq!")) # hello world!


if __name__ == "__main__":
	test()
