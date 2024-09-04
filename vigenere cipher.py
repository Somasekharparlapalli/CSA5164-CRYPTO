def vigenere_cipher(text, key, mode='encrypt'):
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    shift_func = (lambda x, y: (x + y) % 26) if mode == 'encrypt' else (lambda x, y: (x - y + 26) % 26)

    return ''.join(
        chr(shift_func(ord(char) - shift, ord(k) - shift) + shift) if char.isalpha() else char
        for char, k in zip(text, key)
        for shift in [ord('a') if char.islower() else ord('A')]
    )

text = input("Enter a string: ")
key = input("Enter a keyword: ")

encrypted_text = vigenere_cipher(text, key, mode='encrypt')
decrypted_text = vigenere_cipher(encrypted_text, key, mode='decrypt')

print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
