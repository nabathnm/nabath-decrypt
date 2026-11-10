
import os
import sys

EXTENSION = ".dokb"


def decrypt(data):
    result = bytearray(len(data))

    for i in range(len(data)):
        b = data[i] & 0xFF

        result[i] = ((b >> 1) | ((b & 1) << 7)) & 0xFF

    return bytes(result)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 decrypt.py <file{EXTENSION}>")
        sys.exit(1)

    filepath = sys.argv[1]

    if not filepath.endswith(EXTENSION):
        print(f"Error: File must have {EXTENSION} extension.")
        sys.exit(1)

    if not os.path.isfile(filepath):
        print("Error: File not found.")
        sys.exit(1)

    original_name = filepath[:-len(EXTENSION)]

    if os.path.exists(original_name):
        print(f"Error: Output file already exists: {original_name}")
        sys.exit(1)

    with open(filepath, "rb") as f:
        encrypted = f.read()

    decrypted = decrypt(encrypted)

    with open(original_name, "xb") as f:
        f.write(decrypted)

    print(f"Decrypted: {original_name}")


if __name__ == "__main__":
    main()
