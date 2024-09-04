def generate_playfair_matrix(key):
    """Generate Playfair matrix from key."""
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = ''.join(sorted(set(key.upper().replace('J', 'I')), key=key.index))
    return [key + ''.join(ch for ch in alphabet if ch not in key)][0][:25][i:i+5] for i in range(0, 25, 5)]

def preprocess_text(text):
    """Prepare text for Playfair cipher."""
    text = text.upper().replace('J', 'I')
    pairs = [text[i] + (text[i+1] if i+1 < len(text) and text[i] != text[i+1] else 'X') for i in range(0, len(text), 2)]
    return [pair if len(pair) == 2 else pair + 'X' for pair in pairs]

def find_position(matrix, char):
    """Find row and column of char in matrix."""
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)

def playfair_encrypt_pair(pair, matrix):
    """Encrypt a pair of characters."""
    (r1, c1), (r2, c2) = map(lambda p: find_position(matrix, p), pair)
    return (matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]) if r1 == r2 else (matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]) if c1 == c2 else (matrix[r1][c2] + matrix[r2][c1])

def playfair_encrypt(text, matrix):
    """Encrypt text using Playfair cipher."""
    return ''.join(playfair_encrypt_pair(pair, matrix) for pair in preprocess_text(text))


key = "M F H I/J K U N O P Q Z V W X Y E L A R G D S T B C".replace(' ', '')
plaintext = "Must see you over Cadogan West. Coming at once."
matrix = generate_playfair_matrix(key)
ciphertext = playfair_encrypt(plaintext, matrix)

print(f"Playfair Matrix:\n{matrix}")
print(f"Encrypted message: {ciphertext}")
