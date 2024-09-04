def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError(f"'a' = {a} is not coprime with 26.")
    return ''.join(
        chr(((a * (ord(c) - base) + b) % 26) + base) if c.isalpha() else c
        for c in text
        for base in [ord('A') if c.isupper() else ord('a') if c.islower() else None]
    )

try:
    text = input("Text: ")
    a, b = int(input("a: ")), int(input("b: "))
    print("Encrypted:", affine_encrypt(text, a, b))
except ValueError as e:
    print(e)
