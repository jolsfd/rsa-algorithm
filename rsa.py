#!/usr/bin/env python3

import secrets
from typing import List, Tuple
import sympy


def fermat_numbers(n: int) -> int:
    """
    Gibt einer der ersten 5 Fermat Zahlen zurück, die teilerfremd zur Zahl n sind.
    """
    for i in range(5):
        num = 2 ** 2 ** i + 1
        if euclid(num, n) == 1:
            return num

    return -1


def euclid(a: int, b: int) -> int:
    """
    Berechnung des ggT von zwei Zahlen a und b.
    """
    # Rekursiv
    if b == 0:
        return a
    else:
        r = a % b
        return euclid(b, r)


def extended_euclid(a: int, b: int) -> int:
    """
    Erweiterter euklidischer Algorithmus für die Vielfachsummendarstellung.
    """
    # Rekursiv
    if b == 0:
        return a, 1, 0
    else:
        ggT, x, y = extended_euclid(b, a % b)
        x, y = y, x - (a // b) * y
        return ggT, x, y


def modular_inverse(a: int, n: int) -> int:
    """
    Berechnung der modularen Inverse von zwei Zahlen a und n.
    """
    ggT, x, y = extended_euclid(a, n)
    return x % n


def get_random_prime(bits: int) -> int:
    """
    Generiert eine Primzahl mit festgelegter Bitlänge.
    """
    while True:
        num = secrets.randbits(bits)

        if num.bit_length() == bits:
            if sympy.isprime(num):
                return num


class RSA:
    def __init__(self) -> None:
        pass

    def generate_keys(self, bits: int) -> Tuple[Tuple[int]]:
        """
        Generierung von einem öffentlichen und eines privaten Schlüssels mit einer festgelegten Bitlänge des RSA-Moduls.
        """
        while True:
            # (1) Generierung von zwei Primzahlen
            p = get_random_prime(bits // 2)
            q = get_random_prime(bits // 2)

            # (2) Berechnung von n
            n = p * q

            # (3) Auswahl der Zahl e
            phi_n = (p - 1) * (q - 1)
            e = fermat_numbers(phi_n)

            # Wiederholung des Prozesses, wenn e nicht teilerfremd
            if e != -1 and n.bit_length() == bits:

                # (4) Berechnung der Zahl d mithilfe der modularen Inverse
                d = modular_inverse(e, phi_n)

                # DEBUG
                print(n.bit_length(), p.bit_length(), q.bit_length())

                # Geheime Zahlen löschen
                del q, p, phi_n

                return (e, n), (d, n)

    def encrypt(self, m: int, e: int, n: int) -> int:
        """
        Verschlüsseln einer Naricht m mit den Zahlen e und n.
        Rückgabe von -1, wenn Naricht zu lang.
        """
        if m < n:
            # c = m^e mod n
            c = pow(m, e, n)
            return c
        else:
            return -1

    def decrypt(self, c: int, d: int, n: int) -> int:
        """
        Entschlüsseln eines Geheimtextes c mit den Zahlen d und n.
        """
        # m = c^d mod n
        m = pow(c, d, n)
        return m

    def encrypt_text(self, m: str, e: int, n: int) -> List[int]:
        """
        Verschlüsseln eines Textes in beliebger Größe.
        """
        blocks = []
        bits = n.bit_length()
        num_chars = bits // 8 - 1

        for i in range(0, len(m), num_chars):
            chars = m[i : i + num_chars]

            # (1) Mit 0 auffüllen
            #chars = chars + "\0" * (num_chars - len(m))

            # (2) Zeichen in Binär
            binary = "".join(format(ord(i), "08b") for i in chars)

            # (3) Binär in Zahl
            num = int(binary, 2)

            # (4) Verschlüsseln der Zahl
            c = self.decrypt(num, e, n)

            blocks.append(c)

        return blocks

    def decrypt_text(self, blocks: List[int], d: int, n: int) -> str:
        """
        Entschlüsseln eines Textes.
        """
        bits = n.bit_length()
        format_string = f"0{bits}b"
        message_string = ""

        for c in blocks:
            # (1) Entschlüsseln
            m = self.encrypt(c, d, n)

            # (2) Zahl in Binärzahl
            binary = format(m, format_string)

            # (3) Binärzahl in Zeichen
            message_string += "".join(
                chr(int(binary[i : i + 8], 2)) for i in range(0, len(binary), 8)
            )  # generator

        return message_string
