#!/usr/bin/env python3

import argparse
from typing import List, Tuple

from rsa import RSA


def read_key_file(name: str) -> List[int]:
    """
    Schlüssel von Datei lesen.
    """
    file = open(name, "r")

    try:
        lines = file.readlines()

        return [int(line) for line in lines]

    finally:
        file.close()


def write_key_file(name: str, key: List[int]):
    """
    Schlüssel in Datei schreiben.
    """
    file = open(name, "w")

    try:
        [file.write(str(el) + "\n") for el in key]

    finally:
        file.close()


def main():
    # defaults
    default_file = "key.txt"

    rsa = RSA()

    # Main parser
    parser = argparse.ArgumentParser(
        prog="RSA Cli",
        description="Command Line Interface als Beispielhafte Anwendung für RSA",
    )

    # key files
    parser.add_argument(
        "--file",
        type=str,
        default=default_file,
        help="Dateispeicherort für Schlüsseldatei",
    )

    subparsers = parser.add_subparsers(help="sub-command help", dest="command")

    # generate command
    generate_parser = subparsers.add_parser("generate", help="Generate rsa key files")
    generate_parser.add_argument(
        "--bits",
        type=int,
        default=2048,
        help="Länge des RSA-Moduls, welches durch 8 teilbar sein muss",
    )

    # encrypt command
    decrypt_parser = subparsers.add_parser("encrypt", help="Encrypt message")
    decrypt_parser.add_argument("message", type=str, help="Naricht")

    # decrypt command
    encrypt_parser = subparsers.add_parser("decrypt", help="Decrypt message")
    encrypt_parser.add_argument(
        "cipher", type=int, nargs="+", help="Verschlüsselter Text"
    )

    # parse arguments
    args = parser.parse_args()

    if args.command == "generate":
        print(f"Generating RSA key with {args.bits}bits...")

        if args.bits % 8 != 0:
            print("Bits müssen durch 8 teilbar sein!")

        public, private = rsa.generate_keys(args.bits)

        write_key_file(args.file, [public[0], public[1], private[0]])

    elif args.command == "encrypt":
        print(f"Encrypting text message...")

        key = read_key_file(args.file)

        cipher = rsa.encrypt_text(args.message, int(key[0]), int(key[1]))

        print("=" * 20, "Cipher", "=" * 20)
        [print(c, end=" ") for c in cipher]
        print("\n" + "=" * 48)

    elif args.command == "decrypt":
        print(f"Decrypting text message...")

        key = read_key_file(args.file)

        message = rsa.decrypt_text(args.cipher, int(key[2]), int(key[1]))

        print("=" * 20, "Message", "=" * 20)
        print(message)
        print("=" * 49)


if __name__ == "__main__":
    main()
