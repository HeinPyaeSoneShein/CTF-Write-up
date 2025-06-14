import string

# Manual XOR function
def xor_bytes(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

# Encrypted flag (hex -> bytes)
enc_flag = bytes.fromhex("137d0f0c3e76542e193a024d36363a3301211c2d065b30442f2b793b1f1b35413b473b354d0d0533")

# Known part of flag
part_flag = b'THM{'

# Recover first 4 bytes of key using known-plaintext attack
part_key = bytes([enc_flag[i] ^ part_flag[i] for i in range(4)])

# Brute force the last byte of the key (assuming 5-character key)
charset = string.ascii_letters + string.digits

for c in charset:
    key = part_key + c.encode()  # full 5-byte key
    decrypted = xor_bytes(enc_flag, key)

    try:
        decoded = decrypted.decode()
        if decoded.endswith('}'):
            print(f"[+] Key: {key.decode()}")
            print(f"[+] Flag: {decoded}")
    except UnicodeDecodeError:
        continue
