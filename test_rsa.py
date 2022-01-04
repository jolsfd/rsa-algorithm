#!/usr/bin/env python3

import unittest
import rsa
import examples
import random
import sympy


class TestGetRandomPrime(unittest.TestCase):
    def test_random_prime(self):
        """
        Test ob zurückgegebene Primzahl eine Primzahl ist.
        """

        want = True
        get = sympy.isprime(rsa.get_random_prime(128))

        self.assertEqual(want, get)


class TestEuclid(unittest.TestCase):
    def test_coprime(self):
        """
        Testen ob Zahl a teilerfremd zu Zahl b ist.
        """
        want = 1
        get = rsa.euclid(89, 3)
        self.assertEqual(want, get)

    def test_not_coprime(self):
        """
        Testen ob Zahl a nicht teilerfremd zu Zahl b ist.
        """
        want = 5
        get = rsa.euclid(895, 85)
        self.assertEqual(want, get)


class TestExtendedEuclid(unittest.TestCase):
    def test_coprime(self):
        """ """
        want = (1, -29, 5)
        get = rsa.extended_euclid(16, 93)

        self.assertEqual(want, get)


class TestModulareInverse(unittest.TestCase):
    def test_prime(self):
        """ """
        want = 64
        get = rsa.modular_inverse(16, 93)

        self.assertEqual(want, get)


class TestFermatNumbers(unittest.TestCase):
    def test_fermat_number(self):
        """"""

        # (1) Fermat Zahl
        want = 3
        get = rsa.fermat_numbers(4)
        self.assertEqual(want, get)

        # (2) Fermat Zahl
        want = 5
        get = rsa.fermat_numbers(12)
        self.assertEqual(want, get)

        # (3) Fermat Zahl
        want = 17
        get = rsa.fermat_numbers(45)
        self.assertEqual(want, get)

    def test_no_fermat_number(self):
        """"""

        want = -1
        get = rsa.fermat_numbers(3 * 5 * 17 * 257 * 65537)

        self.assertEqual(want, get)


class TestDecrypt(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.n = examples.n
        self.e = examples.e
        self.d = examples.d

        self.rsa = rsa.RSA()

    def test_correct_decrypt(self):
        """
        Test ob Zahl m richig verschlüsselt wird.
        """

        m = 63
        want = 105
        get = self.rsa.decrypt(m, self.e, self.n)

        self.assertEqual(want, get)

    def test_message_too_long(self):
        """
        Test mit zu langer Naricht.
        """
        want = -1
        get = self.rsa.decrypt(
            int.from_bytes(random.randbytes(4097), "big"), self.e, self.n
        )

        self.assertEqual(want, get)


class TestEncrypt(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.n = examples.n
        self.e = examples.e
        self.d = examples.d

        self.rsa = rsa.RSA()

    def test_correct_encrypt(self):
        """
        Test ob Zahl c richtig entschlüsselt wird.
        """

        c = 105
        want = 63
        get = self.rsa.encrypt(c, self.d, self.n)

        self.assertEqual(want, get)


class TestTextDecryption(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.n = examples.n_4096
        self.e = examples.e_4096
        self.d = examples.d_4096

        self.text = "Works for me!"

        self.rsa = rsa.RSA()

    def test_correct_encrypt(self):
        """
        Test ob Text richtig ver- und entschlüsselt wird.
        """

        c_blocks = self.rsa.decrypt_text(self.text, self.e, self.n)
        message = self.rsa.encrypt_text(c_blocks, self.d, self.n)

        self.assertEqual(self.text, message.replace("\0", ""))


if __name__ == "__main__":
    unittest.main()
