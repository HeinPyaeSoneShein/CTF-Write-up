from sympy import factorint
from Crypto.Util.number import inverse

# Given values
n = 340282366920938460843936948965011886881
e = 65537

# Factor n
factors = factorint(n)
p, q = list(factors.keys())

# Compute φ(n)
phi = (p - 1) * (q - 1)

# Compute d
d = inverse(e, phi)
print("Private key d =", d)
