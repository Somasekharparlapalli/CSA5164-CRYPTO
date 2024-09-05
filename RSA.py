from math import gcd

def mod_inverse(a, m):
    """Return the modular inverse of a under modulo m."""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def rsa_private_key(e, n):
    # Step 1: Find p and q
    p, q = None, None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            p = i
            q = n // i
            break
    if p is None or q is None:
        raise ValueError("n is not a product of two primes.")
    
    # Step 2: Compute φ(n)
    phi_n = (p - 1) * (q - 1)
    
    # Step 3: Compute the modular inverse of e modulo φ(n)
    d = mod_inverse(e, phi_n)
    
    return (d, n)

# Get user input
e = int(input("Enter the public exponent (e): "))
n = int(input("Enter the modulus (n): "))

# Compute the private key
try:
    private_key = rsa_private_key(e, n)
    print("Private Key (d, n):", private_key)
except ValueError as ve:
    print(ve)
except Exception as ex:
    print("An error occurred:", ex)
