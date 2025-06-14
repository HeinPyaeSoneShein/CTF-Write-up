# Wiseguy XOR Flag Cracker 🕵️‍♂️

This is a solution script for the XOR-based CTF challenge from TryHackMe's "Wiseguy" room.

It uses a **known-plaintext attack** to recover the XOR encryption key and decrypt the flag.

## 🔧 How It Works

- The challenge gives an XOR-encoded hex string of a flag.
- The first part of the flag is known to be `THM{`.
- The script recovers the key using XOR and brute-forces the last key byte.
- It then decrypts the full flag if it ends with `}`.

## 💡 Example

```bash
$ python3 crack_xor.py
[+] Key: a1b2C
[+] Flag: THM{XOR_is_weak!}
