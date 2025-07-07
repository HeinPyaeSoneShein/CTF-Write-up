🕵️‍♂️ Order – TryHackMe

<img src="https://tryhackme-images.s3.amazonaws.com/room-icons/62ff64c3c859dc0042b2b9f6-1749737621349" alt="Order Room Icon" width="150">
Perform a known-plaintext attack to recover a repeating-key XOR key and decrypt a hidden message.

## Summary

Cipher's message was encrypted with a repeating-key XOR cipher. Since all messages start with `ORDER:`, we used a known-plaintext attack to recover the key and decrypt the full message.

## How to Run

python3 xor_full_decrypt.py
