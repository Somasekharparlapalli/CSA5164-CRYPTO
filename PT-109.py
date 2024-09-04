import re

def create_matrix(keyword):
    """Generate a 5x5 Playfair cipher matrix from the keyword."""
    keyword = ''.join(sorted(set(keyword), key=keyword.index))  # Remove duplicates
    matrix = (keyword + 'ABCDEFGHIKLMNOPQRSTUVWXYZ').replace('J', '')
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, char):
    """Return the position of the character in the matrix."""
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)
    return None

def decrypt_pair(matrix, a, b):
    """Decrypt a pair of characters using the Playfair matrix."""
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    elif c1 == c2:
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    return matrix[r1][c2] + matrix[r2][c1]

def preprocess(text):
    """Prepare text for Playfair cipher: remove non-letters and replace 'J' with 'I'."""
    text = re.sub(r'[^A-Z]', '', text.upper()).replace('J', 'I')
    return text + 'X' * (len(text) % 2)  # Pad with 'X' if odd length

def playfair_decrypt(ciphertext, keyword):
    """Decrypt the ciphertext using the Playfair cipher."""
    matrix = create_matrix(keyword)
    plaintext = ''.join(decrypt_pair(matrix, ciphertext[i], ciphertext[i + 1]) for i in range(0, len(ciphertext), 2))
    return plaintext

def main():
    keyword = input("Enter the keyword: ")
    ciphertext = input("Enter the ciphertext: ").replace(' ', '')
    decrypted_message = playfair_decrypt(preprocess(ciphertext), keyword)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
