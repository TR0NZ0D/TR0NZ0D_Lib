import unittest
from tr0nz0d.security.criptografia import Criptografia


class TestCryptography(unittest.TestCase):
    crypto = Criptografia()
    testing_text = "Testing completed!"

    def test_encrypting(self):
        encrypted_set = self.crypto.criptografar(self.testing_text)
        self.assertEqual(len(encrypted_set), 2)

    def test_decrypting_with_key(self):
        message, key = self.crypto.criptografar(self.testing_text)
        decrypted = self.crypto.descriptografar_com_chave(text=message, custom_key=key)
        self.assertEqual(decrypted, self.testing_text)

    def test_decrypting_with_storage(self):
        message, _ = self.crypto.criptografar(self.testing_text)
        decrypted = self.crypto.descriptografar(message)
        self.assertEqual(decrypted, self.testing_text)


if __name__ == "__main__":
    unittest.main()
