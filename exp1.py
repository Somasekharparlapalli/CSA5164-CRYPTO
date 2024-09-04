def caesar_cipher(text, k):
    return ''.join(
        chr((ord(char) - shift + k) % 26 + shift) if char.isalpha() else char
        for char in text
        for shift in [ord('a') if char.islower() else ord('A')]
    )

text = input("Enter a string: ")
k = int(input("Enter shift value (1-25): "))

encrypted_text = caesar_cipher(text, k)
decrypted_text = caesar_cipher(encrypted_text, -k)

print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
