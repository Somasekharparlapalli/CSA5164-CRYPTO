def create_dict(key):
    """Create a substitution dictionary from the key."""
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if len(key) != len(symbols):
        raise ValueError("Key must be exactly 36 unique characters.")
    return dict(zip(key, symbols))

def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the substitution key."""
    sub_dict = create_dict(key)
    return ''.join(sub_dict.get(char, char) for char in ciphertext)

def main():
    ciphertext = input("Enter the ciphertext: ")
    key = input("Enter the substitution key (36 unique characters): ")
    try:
        plaintext = decrypt(ciphertext, key)
        print("Decrypted plaintext:", plaintext)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
