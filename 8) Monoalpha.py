def create_substitution_dict(keyword):
    """Create a substitution dictionary from the keyword."""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Remove duplicates from keyword while preserving order
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    # Create the cipher alphabet by appending unused letters
    cipher_alphabet = keyword + ''.join(ch for ch in alphabet if ch not in keyword)
    # Create a dictionary mapping each letter of the alphabet to the cipher alphabet
    return dict(zip(alphabet, cipher_alphabet))

def encrypt_message(plaintext, keyword):
    """Encrypt the plaintext using the substitution cipher based on the keyword."""
    sub_dict = create_substitution_dict(keyword)
    plaintext = plaintext.upper()
    return ''.join(sub_dict.get(ch, ch) for ch in plaintext)

def decrypt_message(ciphertext, keyword):
    """Decrypt the ciphertext using the substitution cipher based on the keyword."""
    sub_dict = create_substitution_dict(keyword)
    reverse_sub_dict = {v: k for k, v in sub_dict.items()}
    ciphertext = ciphertext.upper()
    return ''.join(reverse_sub_dict.get(ch, ch) for ch in ciphertext)

# Example usage
keyword = input("Enter the keyword: ")
plaintext = input("Enter the plaintext: ")
encrypted = encrypt_message(plaintext, keyword)
print(f"Encrypted message: {encrypted}")

decrypted = decrypt_message(encrypted, keyword)
print(f"Decrypted message: {decrypted}")
