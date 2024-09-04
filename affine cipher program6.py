def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def solve_affine_equation(c1, c2, p1, p2, m=26):
    a = (c1 - c2) * mod_inverse(p1 - p2, m) % m
    b = (c1 - a * p1) % m
    return a, b

def affine_decrypt(ciphertext, a, b, m=26):
    a_inv = mod_inverse(a, m)
    return ''.join(
        chr((a_inv * (ord(char) - base - b)) % m + base) if char.isalpha() else char
        for char in ciphertext
        for base in [ord('A') if char.isupper() else ord('a')]
    )

# User Input
ciphertext = input("Enter the ciphertext: ")
most_freq_c1 = ord(input("Most frequent ciphertext letter: ").upper()) - ord('A')
second_freq_c2 = ord(input("Second most frequent ciphertext letter: ").upper()) - ord('A')
most_freq_p1, second_freq_p2 = ord('E') - ord('A'), ord('T') - ord('A')

# Solve for 'a' and 'b', and decrypt
a, b = solve_affine_equation(most_freq_c1, second_freq_c2, most_freq_p1, second_freq_p2)
plaintext = affine_decrypt(ciphertext, a, b)

print(f"Solved 'a': {a}, 'b': {b}")
print("Decrypted plaintext:", plaintext)
