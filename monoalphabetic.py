def monoalphabetic_cipher(text, key, decrypt=False):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if decrypt:
        key_map = {key[i]: alphabet[i] for i in range(len(alphabet))}
    else:
        key_map = {alphabet[i]: key[i] for i in range(len(alphabet))}

    return ''.join(key_map[char] if char in key_map else char for char in text.lower())

text = input("Enter a string: ")
key = input("Enter a 26-letter key: ")

# Encrypt
encrypted_text = monoalphabetic_cipher(text, key)

# Decrypt
decrypted_text = monoalphabetic_cipher(encrypted_text, key, decrypt=True)

print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
