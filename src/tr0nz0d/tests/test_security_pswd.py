import unittest
from tr0nz0d.security.pswd import Pass
from random import randint


class TestPasswords(unittest.TestCase):
    passwd = Pass()

    def test_generating_password(self):
        random_int = randint(0, 500)
        gen_pass = self.passwd.gerar(random_int)
        self.assertGreaterEqual(len(gen_pass), random_int)


if __name__ == "__main__":
    unittest.main()
