# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2015-2020 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

Created by: Gabriel Menezes de Antonio (TR0NZ0D)
"""
import unittest

from tr0nz0d.security.criptografia import Criptografia


class TestCryptography(unittest.TestCase):
    """Test case for cryptography"""
    crypto = Criptografia()
    testing_text = "Testing completed!"

    def test_encrypting(self):
        """Test case for encrypting"""
        encrypted_set = self.crypto.criptografar(self.testing_text)
        self.assertEqual(len(encrypted_set), 2)

    def test_decrypting_with_key(self):
        """Test case for decrypting with key"""
        message, key = self.crypto.criptografar(self.testing_text)
        decrypted = self.crypto.descriptografar_com_chave(text=message, custom_key=key)
        self.assertEqual(decrypted, self.testing_text)

    def test_decrypting_with_storage(self):
        """Test case for decrypting with storage"""
        message, _ = self.crypto.criptografar(self.testing_text)
        decrypted = self.crypto.descriptografar(message)
        self.assertEqual(decrypted, self.testing_text)


if __name__ == "__main__":
    unittest.main()
