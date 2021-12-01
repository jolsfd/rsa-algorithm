import unittest
import rsa


class TestEuclid(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(rsa.euclid(89, 3), 1)

    def test_not_prime(self):
        self.assertEqual(rsa.euclid(24, 8), 8)
        self.assertEqual(rsa.euclid(90, 25), 5)
        self.assertEqual(rsa.euclid(-65, 89), 1)

    def test_special_cases(self):
        self.assertEqual(rsa.euclid(1, 1), 1)
        self.assertEqual(rsa.euclid(0, 1), 1)
        self.assertEqual(rsa.euclid(1, 0), 1)


class TestExtendedEuclid(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(rsa.extended_euclid(15, 71), (1, 19, -4))

    def test_not_prime(self):
        self.assertEqual(rsa.extended_euclid(65, 100), (5, -3, 2))
        self.assertEqual(rsa.extended_euclid(-85, 45), (5, 1, 2))

    def test_special_cases(self):
        self.assertEqual(rsa.extended_euclid(1, 1), (1, 0, 1))
        self.assertEqual(rsa.extended_euclid(1, 0), (1, 1, 0))
        self.assertEqual(rsa.extended_euclid(0, 1), (1, 0, 1))


class TestModulareInverse(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(rsa.modular_inverse(89, 65), 19)

    def test_not_prime(self):
        self.assertEqual(rsa.modular_inverse(45, 85), 2)


class TestFermatNumbers(unittest.TestCase):
    def test_fermat_number(self):
        self.assertEqual(rsa.fermat_numbers(4), 3)
        self.assertEqual(rsa.fermat_numbers(12), 5)
        self.assertEqual(rsa.fermat_numbers(45), 17)
        self.assertEqual(rsa.fermat_numbers(567454560), 257)


class TestDecrypt(unittest.TestCase):
    def test_correct_decrypt(self):
        public = (5, 270396079058430727)

        c = 9167575457715517
        m = 10304003

        self.assertEqual(rsa.decrypt(m, public[0], public[1]), c)

    def test_message_too_long(self):
        public = (5, 270396079058430727)

        m_long = 270396079058430728

        self.assertEqual(rsa.decrypt(m_long, public[0], public[1]), -1)


class TestEncrypt(unittest.TestCase):
    def test_correct_cipher(self):
        private = (216316862368315661, 270396079058430727)

        c = 9167575457715517
        m = 10304003

        self.assertEqual(rsa.encrypt(c, private[0], private[1]), m)

    def test_wrong_cipher(self):
        private = (216316862368315661, 270396079058430727)

        c_wrong = 91675754565715517
        m = 10304003

        self.assertNotEqual(rsa.encrypt(c_wrong, private[0], private[1]), m)


class TestGenerateKeys(unittest.TestCase):
    def test_key_generation(self):
        rsa.generate_keys(8)


if __name__ == "__main__":
    unittest.main()
