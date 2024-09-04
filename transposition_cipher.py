import math

def transposition_cipher(text, key, mode='encrypt'):
    num_columns = len(key)
    num_rows = math.ceil(len(text) / num_columns)
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    if mode == 'encrypt':
        # Fill grid with plaintext
        for i, char in enumerate(text):
            grid[i // num_columns][i % num_columns] = char
        # Read columns based on key order
        sorted_indices = sorted(range(num_columns), key=lambda k: key[k])
        return ''.join(grid[r][c] for c in sorted_indices for r in range(num_rows))
    elif mode == 'decrypt':
        sorted_indices = sorted(range(num_columns), key=lambda k: key[k])
        for i, c in enumerate(text):
            grid[i % num_rows][sorted_indices[i // num_rows]] = c
        return ''.join(''.join(row) for row in grid).strip()

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key (unique characters): ")

    encrypted = transposition_cipher(plaintext, key, 'encrypt')
    print(f"Encrypted message: {encrypted}")

    decrypted = transposition_cipher(encrypted, key, 'decrypt')
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
