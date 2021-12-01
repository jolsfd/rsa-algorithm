import secrets
from Crypto.Math.Primality import miller_rabin_test


def fermat_numbers(n: int) -> int:
    for i in range(5):
        fermat_number = 2 ** 2 ** i + 1
        if euclid(fermat_number, n) == 1:
            return fermat_number

    return -1


def euclid(a, b):
    # Rekursiv
    if b == 0:
        return a
    else:
        r = a % b
        return euclid(b, r)


def extended_euclid(a, b):
    # Rekursiv
    if b == 0:
        return a, 1, 0
    else:
        ggT, x, y = extended_euclid(b, a % b)
        x, y = y, x - (a // b) * y
        return ggT, x, y


def modular_inverse(a, n):
    ggT, x, y = extended_euclid(a, n)
    return x % n


def generate_keys(bits: int):
    while True:
        # Generate p
        while True:
            p = secrets.randbits(bits)
            if miller_rabin_test(p, 40):
                break

        # Generate q
        while True:
            q = secrets.randbits(bits)
            if miller_rabin_test(q, 40):
                break

        # Generate N
        n = p * q

        # Generate phi N
        phi_n = (p - 1) * (q - 1)

        e = fermat_numbers(phi_n)

        # If an error occures restart key generation.
        if e == -1:
            continue

        # Generate d
        d = modular_inverse(e, phi_n)

        print(n.bit_length())

        # Delete secrets
        del q, p, phi_n

        return (e, n), (d, n)


def encrypt(c: int, d: int, n: int) -> int:
    m = pow(c, d, n)  # m = c^d mod n
    return m


def decrypt(m: int, e: int, n: int) -> int:
    if m < n:
        c = pow(m, e, n)  # c = m^e mod n
        return c
    else:
        return -1
