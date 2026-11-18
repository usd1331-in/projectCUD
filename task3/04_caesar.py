def shift_char(c, key):
    if c.isupper():
        return chr((ord(c) - ord('A') + key) % 26 + ord('A'))
    if c.islower():
        return chr((ord(c) - ord('a') + key) % 26 + ord('a'))
    return c

def encrypt(text, key):
    return "".join(shift_char(c, key) for c in text)

def decrypt(text, key):
    return encrypt(text, -key)

message = "MEET AT THE LIBRARY AT NOON"
key = 7

cipher = encrypt(message, key)
print("plaintext:", message)
print("key:", key)
print("ciphertext:", cipher)
print("decrypted:", decrypt(cipher, key))

print("\nbrute force all keys:")
for k in range(1, 26):
    print(k, decrypt(cipher, k))

print("\nletter frequency:")
freq = {}
for c in cipher:
    if c.isalpha():
        freq[c] = freq.get(c, 0) + 1
for letter, count in sorted(freq.items(), key=lambda x: -x[1]):
    print(letter, count)
