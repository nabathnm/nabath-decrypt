import os
import sys

KEY = b"H8EmHFHxpZtQgolRjOa2szZBaHELL0L4DYTNZxHmeV2kahWMOt97doKiNCPwUWjfvhm4hCiYDjoQbytOanQRpaA0nxSZZLsorGjSP2aQNxIXyr4rpdfSVZRik6ROl7XCBkeBOzWZH=="
EXTENSION = ".dokb"

def decrypt(data):
    unshifted = bytearray(len(data))
    for i in range(len(data)):
        b = data[i] & 0xFF
        unshifted[i] = ((b >> 1) | (b << 7)) & 0xFF

    result = bytearray(len(unshifted))
    for i in range(len(unshifted)):
        result[i] = unshifted[i] ^ KEY[i % len(KEY)]

    return bytes(result)

if len(sys.argv) < 2:
    print(f"Usage: python3 script.py <file{EXTENSION}>")
    sys.exit(1)

filepath = sys.argv[1]

with open(filepath, "rb") as f:
    encrypted = f.read()

decrypted = decrypt(encrypted)
original_name = filepath[:-len(EXTENSION)]

with open(original_name, "wb") as f:
    f.write(decrypted)

print(f"Decrypted: {original_name}")
