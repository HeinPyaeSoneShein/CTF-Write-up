# xor_full_decrypt.py

# Combined ciphertext
combined_hex = "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f63731a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"
combined_bytes = bytes.fromhex(combined_hex)

# Known plaintext header
known_header = b"ORDER:"

# Recover XOR key
key = bytes([combined_bytes[i] ^ known_header[i] for i in range(len(known_header))])
print("[+] Recovered key:", key)

# Decrypt function
def xor_decrypt(ciphertext: bytes, key: bytes) -> str:
    return ''.join(chr(c ^ key[i % len(key)]) for i, c in enumerate(ciphertext))

# Decrypt and print
decrypted_full = xor_decrypt(combined_bytes, key)
print("\n[+] Fully Decrypted Message:")
print(decrypted_full)
